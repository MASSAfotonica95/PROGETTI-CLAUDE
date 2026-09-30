"""Caricamento del registro delle fonti (JSON). Nuove fonti = nuovi file .json, nessun codice."""
from __future__ import annotations

import json
from pathlib import Path

DEFAULT_DIR = Path(__file__).parent / "sources"


def load_sources(extra_dirs: list[str] | None = None) -> list[dict]:
    out: dict[str, dict] = {}
    for d in [DEFAULT_DIR, *(Path(p) for p in (extra_dirs or []))]:
        for f in sorted(d.glob("*.json")):
            for s in json.loads(f.read_text(encoding="utf-8"))["sources"]:
                out[s["id"]] = s  # un file utente può sovrascrivere una fonte di default
    return list(out.values())


def applies(source: dict, lat: float, lon: float, context: dict) -> bool:
    from .geo import bbox_contains
    if source.get("bbox") and not bbox_contains(source["bbox"], lat, lon):
        return False
    cond = source.get("applies_if", {})
    if "comune" in cond:
        c = (context.get("comune") or "").lower()
        if c not in [x.lower() for x in cond["comune"]]:
            return False
    if "provincia" in cond:
        if context.get("provincia"):
            prov = context["provincia"].lower().replace("provincia di ", "").replace("provincia autonoma di ", "")
            if prov not in [x.lower() for x in cond["provincia"]]:
                return False
    if "regione" in cond and context.get("regione"):
        r = context["regione"].lower()
        if r not in [x.lower() for x in cond["regione"]]:
            return False
    return True
