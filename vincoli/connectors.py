"""Connettori per i tipi di servizio: ArcGIS REST, WFS (GeoServer/CQL), WMS GetFeatureInfo,
geocodifica inversa e fonti solo documentali.

Regola di onestà: un livello è NO_HIT solo se il servizio ha risposto correttamente
con zero elementi. Qualunque errore/ambiguità -> UNVERIFIED, mai "nessun vincolo".
"""
from __future__ import annotations

import math
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urlencode

import requests

from .models import Finding, Point, Status


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _base(source: dict, layer: dict) -> Finding:
    return Finding(
        source_id=source["id"], source_name=source["name"], layer=layer["name"],
        theme=layer.get("theme", source.get("theme", "")), status=Status.UNVERIFIED,
        legal_ref=layer.get("legal_ref", source.get("legal_ref", "")),
        provider=source.get("provider", ""), value_note=source.get("value_note", ""),
        queried_at=_now())


def _summarize(attrs: dict, fields: list[str] | None) -> str:
    keys = fields or list(attrs)[:6]
    return "; ".join(f"{k}={attrs[k]}" for k in keys if attrs.get(k) not in (None, "", " "))


def _links(attrs: dict, link_fields: list[str] | None) -> list[str]:
    return [attrs[k] for k in (link_fields or []) if isinstance(attrs.get(k), str) and attrs[k].startswith("http")]


def _fill(f: Finding, rows: list[dict], layer: dict, status: Status) -> Finding:
    f.status = status if rows else Status.NO_HIT
    f.attributes = rows
    f.summary = [_summarize(r, layer.get("display_fields")) for r in rows]
    for r in rows:
        f.links += _links(r, layer.get("link_fields"))
    return f


def _fail(f: Finding, exc: Exception | str) -> Finding:
    f.status = Status.UNVERIFIED
    f.detail = f"{type(exc).__name__}: {exc}" if isinstance(exc, Exception) else str(exc)
    return f


# --------------------------------------------------------------------------- ArcGIS REST
def query_arcgis(session, source: dict, layer: dict, pt: Point, radius_m: float = 0, timeout=30) -> Finding:
    f = _base(source, layer)
    url = f"{source['url'].rstrip('/')}/{layer['id']}/query"
    params = {
        "geometry": f"{pt.lon},{pt.lat}", "geometryType": "esriGeometryPoint", "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects", "outFields": layer.get("out_fields", "*"),
        "returnGeometry": "false", "f": "json",
    }
    if radius_m > 0:
        params.update(distance=radius_m, units="esriSRUnit_Meter")
    f.query_url = f"{url}?{urlencode(params)}"
    try:
        r = session.get(url, params=params, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        if "error" in data:
            return _fail(f, f"errore servizio: {data['error']}")
        rows = [ft.get("attributes", {}) for ft in data.get("features", [])]
        return _fill(f, rows, layer, Status.NEARBY if radius_m > 0 else Status.HIT)
    except (requests.RequestException, ValueError) as e:
        return _fail(f, e)


# --------------------------------------------------------------------------- WFS (GeoServer)
def query_wfs(session, source: dict, layer: dict, pt: Point, radius_m: float = 0, timeout=30) -> Finding:
    """Usa CQL con EWKT 'SRID=4326;POINT(lon lat)': senza SRID esplicito GeoServer interpreta
    le coordinate nel CRS nativo del layer (verificato sul servizio ISPRA: risultato vuoto)."""
    f = _base(source, layer)
    geom = layer.get("geometry_field", "geom")
    wkt = f"SRID=4326;POINT({pt.lon} {pt.lat})"
    cql = (f"DWITHIN({geom},{wkt},{radius_m},meters)" if radius_m > 0 else f"INTERSECTS({geom},{wkt})")
    params = {"service": "WFS", "version": source.get("wfs_version", "2.0.0"), "request": "GetFeature",
              "typeNames": layer["typename"], "outputFormat": "application/json",
              "count": layer.get("max_features", 20), "CQL_FILTER": cql}
    f.query_url = f"{source['url']}?{urlencode(params)}"
    try:
        r = session.get(source["url"], params=params, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        rows = [ft.get("properties", {}) for ft in data.get("features", [])]
        return _fill(f, rows, layer, Status.NEARBY if radius_m > 0 else Status.HIT)
    except (requests.RequestException, ValueError) as e:
        return _fail(f, e)


# --------------------------------------------------------------------------- WMS GetFeatureInfo
def query_wms(session, source: dict, layer: dict, pt: Point, radius_m: float = 0, timeout=30) -> Finding:
    """ATTENZIONE: GetFeatureInfo applica una tolleranza in pixel -> risultato APPROSSIMATO.
    Si riduce la tolleranza usando un bbox di ~20 m e 101x101 px; preferire WFS/ArcGIS se disponibili."""
    f = _base(source, layer)
    half = max(radius_m, 10.0)
    dlat = half / 111_320.0
    dlon = half / (111_320.0 * math.cos(math.radians(pt.lat)))
    # WMS 1.3.0 + EPSG:4326 => ordine assi lat,lon
    bbox = f"{pt.lat - dlat},{pt.lon - dlon},{pt.lat + dlat},{pt.lon + dlon}"
    params = {"service": "WMS", "version": "1.3.0", "request": "GetFeatureInfo", "layers": layer["name_wms"],
              "query_layers": layer["name_wms"], "styles": "", "info_format": "application/json",
              "crs": "EPSG:4326", "bbox": bbox, "width": 101, "height": 101, "i": 50, "j": 50,
              "feature_count": 20}
    f.query_url = f"{source['url']}?{urlencode(params)}"
    f.detail = "Precisione approssimata (tolleranza pixel del GetFeatureInfo)."
    try:
        r = session.get(source["url"], params=params, timeout=timeout)
        r.raise_for_status()
        if "json" not in r.headers.get("content-type", ""):
            return _fail(f, f"risposta non JSON: {r.text[:120]!r}")
        rows = [ft.get("properties", {}) for ft in r.json().get("features", [])]
        return _fill(f, rows, layer, Status.HIT)
    except (requests.RequestException, ValueError) as e:
        return _fail(f, e)


CONNECTORS = {"arcgis": query_arcgis, "wfs": query_wfs, "wms": query_wms}


# --------------------------------------------------------------------------- contesto amministrativo
def reverse_geocode(session, pt: Point, timeout=30) -> dict[str, Any]:
    """Nominatim/OSM (ODbL). Solo contesto (comune, regione): non è un vincolo."""
    try:
        r = session.get("https://nominatim.openstreetmap.org/reverse", timeout=timeout,
                        params={"format": "jsonv2", "lat": pt.lat, "lon": pt.lon, "zoom": 16,
                                "addressdetails": 1, "accept-language": "it"})
        r.raise_for_status()
        d = r.json()
        a = d.get("address", {})
        return {"ok": True, "display_name": d.get("display_name"),
                "comune": a.get("city") or a.get("town") or a.get("village") or a.get("municipality"),
                "provincia": a.get("county") or a.get("state_district"), "regione": a.get("state"),
                "strada": a.get("road"), "cap": a.get("postcode"), "paese": a.get("country_code"),
                "fonte": "OpenStreetMap Nominatim (ODbL)"}
    except (requests.RequestException, ValueError) as e:
        return {"ok": False, "detail": f"{type(e).__name__}: {e}"}


def manual_finding(source: dict, item: dict) -> Finding:
    return Finding(
        source_id=source["id"], source_name=source["name"], layer=item["name"],
        theme=item.get("theme", source.get("theme", "")), status=Status.MANUAL,
        legal_ref=item.get("legal_ref", ""), provider=source.get("provider", ""),
        links=[item["url"]] if item.get("url") else [], detail=item.get("how", ""),
        value_note=item.get("value_note", source.get("value_note", "")), queried_at=_now())
