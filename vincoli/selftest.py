"""Autotest dei livelli: controllo positivo con un punto certamente interno a un elemento reale.

Senza questo controllo un 'nessun elemento' non dimostra nulla (il livello potrebbe essere vuoto, rinominato o rotto).
Esito per livello: OK (il servizio restituisce l'elemento), FAIL (non lo restituisce / errore), VUOTO (livello senza elementi).
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import requests

from .connectors import query_arcgis
from .geo import utm_to_latlon
from .http import make_session
from .models import Point, Status
from .registry import load_sources


def _inside(pt, ring):
    x, y = pt
    c = False
    for (x1, y1), (x2, y2) in zip(ring, ring[1:]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


def interior_candidates(geom: dict, limit=6):
    """Fino a `limit` punti interni (poligoni: prima triangoli di vertici consecutivi, poi griglia sul bbox)."""
    if "x" in geom or geom.get("points") or geom.get("paths"):
        p = interior_point(geom)
        return [p] if p else []
    rings = geom.get("rings") or []
    inpoly = lambda q: sum(_inside(q, r) for r in rings) % 2 == 1  # noqa: E731
    out = []
    for ring in sorted(rings, key=len, reverse=True)[:3]:
        step = max(1, len(ring) // 200)
        for i in range(0, len(ring) - 2, step):
            c = tuple(sum(v) / 3 for v in zip(ring[i][:2], ring[i + 1][:2], ring[i + 2][:2]))
            if inpoly(c):
                out.append(c)
                if len(out) >= limit:
                    return out
    if len(out) < limit and rings:
        xs = [p[0] for r in rings for p in r]
        ys = [p[1] for r in rings for p in r]
        n = 25
        for i in range(1, n):
            for j in range(1, n):
                c = (min(xs) + (max(xs) - min(xs)) * i / n, min(ys) + (max(ys) - min(ys)) * j / n)
                if inpoly(c):
                    out.append(c)
                    if len(out) >= limit:
                        return out
    return out


def interior_point(geom: dict):
    """Punto interno (o sul tracciato) di una geometria ArcGIS JSON in WGS84."""
    if "x" in geom:
        return geom["x"], geom["y"]
    if "points" in geom and geom["points"]:
        return tuple(geom["points"][0][:2])
    if "paths" in geom and geom["paths"]:
        p = max(geom["paths"], key=len)
        if len(p) >= 2:
            return (p[0][0] + p[1][0]) / 2, (p[0][1] + p[1][1]) / 2
        return tuple(p[0][:2])
    rings = geom.get("rings") or []
    if not rings:
        return None
    inpoly = lambda q: sum(_inside(q, r) for r in rings) % 2 == 1  # noqa: E731  (even-odd: gestisce i buchi)
    for ring in sorted(rings, key=len, reverse=True)[:5]:
        step = max(1, len(ring) // 400)
        for i in range(0, len(ring) - 2, step):
            c = tuple(sum(v) / 3 for v in zip(ring[i][:2], ring[i + 1][:2], ring[i + 2][:2]))
            if inpoly(c):
                return c
    return None


def _fetch_one(session, url, generalize, timeout):
    """Un elemento con geometria; se il server non supporta resultRecordCount si passa da returnIdsOnly."""
    base = {"outFields": "*", "returnGeometry": "true", "outSR": 4326, "f": "json"}
    if generalize:
        base.update(maxAllowableOffset=0.0002, geometryPrecision=6)
    d = session.get(url, params={**base, "where": "1=1", "resultRecordCount": 1}, timeout=timeout).json()
    if "error" in d and "agination" in str(d["error"].get("message")):
        ids = session.get(url, params={"where": "1=1", "returnIdsOnly": "true", "f": "json"}, timeout=timeout).json()
        oids = ids.get("objectIds") or []
        if not oids:
            return {"features": []}
        d = session.get(url, params={**base, "objectIds": oids[0]}, timeout=timeout).json()
    return d


def to_wgs84(x, y):
    """(lon, lat) da coordinate in gradi oppure, se fuori range, UTM 32N ETRS89 (difetto di alcuni servizi che ignorano outSR)."""
    if abs(x) <= 180 and abs(y) <= 90:
        return x, y
    if 100_000 < x < 900_000 and 4_000_000 < y < 6_000_000:
        lat, lon = utm_to_latlon(x, y, 32)
        return lon, lat
    return None


def _probe_by_extent(session, url, timeout, distance=0):
    """Per server che non restituiscono la geometria: estensione di un elemento + ricerca a griglia di un punto che il
    servizio stesso riconosce come interno a quell'elemento (il controllo verifica comunque che il livello sia interrogabile)."""
    ids = session.get(url, params={"where": "1=1", "returnIdsOnly": "true", "f": "json"}, timeout=timeout).json().get("objectIds") or []
    if not ids:
        return None
    for oid in ids[:3]:
        ext = session.get(url, params={"objectIds": oid, "returnExtentOnly": "true", "outSR": 4326, "f": "json"}, timeout=timeout).json().get("extent")
        if not ext:
            continue
        n = 15
        cells = sorted(((i, j) for i in range(n + 1) for j in range(n + 1)), key=lambda t: abs(t[0] - n / 2) + abs(t[1] - n / 2))
        for i, j in cells:
            x = ext["xmin"] + (ext["xmax"] - ext["xmin"]) * i / n
            y = ext["ymin"] + (ext["ymax"] - ext["ymin"]) * j / n
            ll = to_wgs84(x, y)
            if ll is None:
                continue
            q = {"geometry": f"{ll[0]},{ll[1]}", "geometryType": "esriGeometryPoint", "inSR": 4326,
                 "spatialRel": "esriSpatialRelIntersects", "objectIds": oid, "returnCountOnly": "true", "f": "json"}
            if distance:
                q.update(distance=distance, units="esriSRUnit_Meter")
            r = session.get(url, params=q, timeout=timeout).json()
            if r.get("count"):
                return ll
    return None


def check_layer(session, source: dict, layer: dict, timeout=60) -> dict:
    res = {"source": source["id"], "layer": layer["name"], "id": layer["id"]}
    url = f"{source['url'].rstrip('/')}/{layer['id']}/query"
    why = "geometria non utilizzabile"
    for generalize in (True, False):
        try:
            d = _fetch_one(session, url, generalize, timeout)
        except (requests.RequestException, ValueError) as e:
            return {**res, "esito": "FAIL", "dettaglio": f"{type(e).__name__}"}
        if "error" in d:
            return {**res, "esito": "FAIL", "dettaglio": str(d["error"].get("message"))[:80]}
        feats = d.get("features", [])
        if not feats:
            return {**res, "esito": "VUOTO", "dettaglio": "nessun elemento nel livello"}
        geom = feats[0].get("geometry")
        if not geom:
            continue
        for pt in interior_candidates(geom):
            ll = to_wgs84(pt[0], pt[1])
            if ll is None:
                why = "coordinate non convertibili"
                continue
            pt = ll
            f = query_arcgis(session, source, layer, Point(pt[1], pt[0]), 0, timeout)
            if f.status in (Status.HIT, Status.NEARBY):
                return {**res, "esito": "OK", "dettaglio": f"{len(f.attributes)} elementi sul punto di controllo"}
            why = "il servizio non restituisce l'elemento sul suo stesso punto" if f.status == Status.NO_HIT else f"errore: {f.detail[:60]}"
    try:
        pt = _probe_by_extent(session, url, timeout, layer.get("proximity_m", 0))
    except (requests.RequestException, ValueError):
        pt = None
    if pt:
        f = query_arcgis(session, source, layer, Point(pt[1], pt[0]), 0, timeout)
        if f.status in (Status.HIT, Status.NEARBY):
            return {**res, "esito": "OK", "dettaglio": f"{len(f.attributes)} elementi sul punto di controllo (via estensione)"}
        why = "il servizio non restituisce l'elemento sul punto di controllo (via estensione)"
    return {**res, "esito": "FAIL", "dettaglio": why}


def _safe(session, s, l):
    try:
        return check_layer(session, s, l)
    except Exception as e:  # noqa: BLE001  (l'autotest non deve interrompersi per un singolo livello)
        return {"source": s["id"], "layer": l["name"], "id": l["id"], "esito": "FAIL", "dettaglio": f"{type(e).__name__}: {e}"[:90]}


def run_selftest(only=None, extra_dirs=None, workers=8) -> list[dict]:
    session = make_session()
    jobs = [(s, l) for s in load_sources(extra_dirs) if s["type"] == "arcgis" and (not only or s["id"] in only)
            for l in s["layers"]]
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda j: _safe(session, *j), jobs))
