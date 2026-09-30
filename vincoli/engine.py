from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from .connectors import CONNECTORS, manual_finding, reverse_geocode
from .http import make_session
from .models import Finding, Point, Status
from .registry import applies, load_sources


def _key(attrs: dict) -> str:
    return repr(sorted(attrs.items()))


def run(pt: Point, radius_m: float = 0, extra_dirs: list[str] | None = None,
        only: list[str] | None = None, workers: int = 8, timeout: int = 30,
        geocode: bool = True, include_info: bool = False) -> dict:
    session = make_session()
    context = reverse_geocode(session, pt, timeout) if geocode else {"ok": False, "detail": "disattivata"}
    sources = [s for s in load_sources(extra_dirs) if not only or s["id"] in only]

    tasks, findings, skipped_info = [], [], 0
    for s in sources:
        if not applies(s, pt.lat, pt.lon, context):
            # Se il comune non è noto (geocodifica fallita) le fonti condizionate al comune restano da verificare.
            if s.get("applies_if", {}).get("comune") and not context.get("comune") and not s.get("bbox"):
                pass
            else:
                continue
        if s["type"] == "manual":
            findings += [manual_finding(s, it) for it in s["items"]]
            continue
        fn = CONNECTORS[s["type"]]
        for layer in s["layers"]:
            if layer.get("info") and not include_info:
                skipped_info += 1
                continue
            tasks.append((fn, s, layer))

    def job(t):
        fn, s, layer = t
        f = fn(session, s, layer, pt, 0, timeout)
        if radius_m > 0 and f.status in (Status.NO_HIT, Status.HIT):
            g = fn(session, s, layer, pt, radius_m, timeout)
            if g.status == Status.UNVERIFIED:
                f.detail = (f.detail + " " if f.detail else "") + f"Ricerca nel raggio di {radius_m:g} m non riuscita: {g.detail}"
            else:
                seen = {_key(a) for a in f.attributes}
                extra = [(a, sm) for a, sm in zip(g.attributes, g.summary) if _key(a) not in seen]
                if extra:
                    n = Finding(**{**f.__dict__, "status": Status.NEARBY,
                                   "attributes": [a for a, _ in extra], "summary": [s_ for _, s_ in extra],
                                   "links": [], "query_url": g.query_url,
                                   "detail": f"Non sul punto ma entro {radius_m:g} m."})
                    n.links = g.links
                    return [f, n]
        return [f]

    with ThreadPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(job, tasks):
            findings += res

    order = {Status.HIT: 0, Status.NEARBY: 1, Status.UNVERIFIED: 2, Status.MANUAL: 3, Status.NO_HIT: 4, Status.NOT_APPLICABLE: 5}
    findings.sort(key=lambda f: (order[f.status], f.theme, f.layer))
    return {"point": {"lat": pt.lat, "lon": pt.lon}, "radius_m": radius_m, "context": context,
            "findings": findings, "queried_layers": len(tasks), "skipped_info_layers": skipped_info}
