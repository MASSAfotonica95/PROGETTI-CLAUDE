from __future__ import annotations

import json
from collections import Counter

from .geo import latlon_to_utm
from .models import Status

CAVEAT = ("Esito ricognitivo a scopo conoscitivo: NON ha valore certificativo. "
          "\"Nessun elemento\" vale solo per il livello interrogato e solo se il servizio ha risposto. "
          "Per valore probatorio: Certificato di Destinazione Urbanistica (art. 30 DPR 380/2001) e atti originari.")

ICON = {Status.HIT: "🔴", Status.NEARBY: "🟠", Status.UNVERIFIED: "⚠️", Status.MANUAL: "📄", Status.NO_HIT: "🟢"}


def to_json(result: dict) -> str:
    return json.dumps({**result, "findings": [f.to_dict() for f in result["findings"]],
                       "avvertenza": CAVEAT}, ensure_ascii=False, indent=2)


def to_markdown(result: dict) -> str:
    p, ctx, fs = result["point"], result["context"], result["findings"]
    e32 = latlon_to_utm(p["lat"], p["lon"], 32)
    e33 = latlon_to_utm(p["lat"], p["lon"], 33)
    L = [f"# Verifica vincoli – {p['lat']:.6f}, {p['lon']:.6f}", ""]
    L.append(f"- WGS84 (EPSG:4326): {p['lat']:.9f}, {p['lon']:.9f}")
    L.append(f"- ETRS89/UTM 32N (EPSG:25832): E {e32[0]:.3f} N {e32[1]:.3f} · UTM 33N (EPSG:25833): E {e33[0]:.3f} N {e33[1]:.3f}")
    if ctx.get("ok"):
        L.append(f"- Località (da {ctx['fonte']}, indicativa): {ctx.get('strada') or '-'}, {ctx.get('comune') or '-'} "
                 f"({ctx.get('provincia') or '-'}), {ctx.get('regione') or '-'}")
    else:
        L.append(f"- Località: **non determinata** ({ctx.get('detail')})")
    if result["radius_m"]:
        L.append(f"- Raggio di ricerca aggiuntivo: {result['radius_m']:g} m")
    if result.get("queried_layers") is not None:
        L.append(f"- Livelli interrogati: {result['queried_layers']}" + (f" (+{result['skipped_info_layers']} informativi non interrogati: opzione --all)" if result.get("skipped_info_layers") else ""))
    c = Counter(f.status for f in fs)
    L += ["", "**Riepilogo:** " + " · ".join(f"{ICON[s]} {s.value}: {c[s]}" for s in ICON if c[s]), "", f"> {CAVEAT}", ""]

    def section(title, statuses, detail=True):
        rows = [f for f in fs if f.status in statuses]
        if not rows:
            return
        L.append(f"## {title}")
        last_theme = None
        for f in sorted(rows, key=lambda x: (x.theme, x.layer)):
            if f.theme != last_theme:
                L.append(f"#### Tema: {f.theme or '—'}")
                last_theme = f.theme
            L.append(f"### {ICON[f.status]} {f.layer}")
            L.append(f"- Stato: **{f.status.value}** · Tema: {f.theme}" + (f" · Norma: {f.legal_ref}" if f.legal_ref else ""))
            L.append(f"- Fonte: {f.source_name} ({f.provider})")
            if detail:
                for s in f.summary:
                    L.append(f"  - {s}")
                for l in dict.fromkeys(f.links):
                    L.append(f"  - Documento: {l}")
            if f.detail:
                L.append(f"- Nota: {f.detail}")
            if f.value_note:
                L.append(f"- Valore del dato: {f.value_note}")
            if f.query_url and f.status != Status.MANUAL:
                L.append(f"- Query (riproducibile, {f.queried_at}): <{f.query_url}>")
            if f.status == Status.MANUAL and f.links:
                L.append(f"- Link: {f.links[0]}")
        L.append("")

    section("Vincoli intercettati sul punto", {Status.HIT})
    section("Elementi entro il raggio", {Status.NEARBY})
    section("NON VERIFICATI (servizio non disponibile)", {Status.UNVERIFIED})
    section("Da verificare manualmente (nessuna API)", {Status.MANUAL})
    clear = [f for f in fs if f.status == Status.NO_HIT]
    if clear:
        L.append("## Livelli interrogati senza elementi sul punto")
        L += [f"- {f.layer} — {f.source_name}" for f in clear]
    return "\n".join(L) + "\n"
