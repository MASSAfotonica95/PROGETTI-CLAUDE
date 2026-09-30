from __future__ import annotations

import argparse
import sys

from .engine import run
from .geo import parse_coordinate, utm_to_latlon
from .models import Point
from .registry import load_sources
from .report import to_json, to_markdown


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="vincoli", description="Vincoli territoriali su una coordinata")
    ap.add_argument("coord", nargs="?", help="'lat,lon' WGS84 (gradi decimali)")
    ap.add_argument("--utm", nargs=3, metavar=("E", "N", "ZONA"), help="coordinate UTM ETRS89 (zona 32 o 33)")
    ap.add_argument("--radius", type=float, default=0, help="raggio in metri per elementi vicini")
    ap.add_argument("--format", choices=("md", "json"), default="md")
    ap.add_argument("--only", nargs="*", help="limita a id fonte")
    ap.add_argument("--sources-dir", action="append", help="cartella con ulteriori registri .json")
    ap.add_argument("--no-geocode", action="store_true", help="non usare Nominatim")
    ap.add_argument("--all", action="store_true", help="includi anche i livelli informativi/di contesto")
    ap.add_argument("--list-sources", action="store_true")
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--selftest", action="store_true", help="controllo positivo di ogni livello (punto noto)")
    a = ap.parse_args(argv)

    if a.selftest:
        from collections import Counter
        from .selftest import run_selftest
        rows = run_selftest(a.only, a.sources_dir)
        for r in rows:
            if r["esito"] != "OK":
                print(f"{r['esito']:6} {r['source']}/{r['id']} {r['layer'][:60]} – {r['dettaglio']}")
        c = Counter(r["esito"] for r in rows)
        print(f"\nTotale {len(rows)}: " + ", ".join(f"{k}={v}" for k, v in c.items()))
        return 0 if not c.get("FAIL") else 1

    if a.list_sources:
        for s in load_sources(a.sources_dir):
            print(f"{s['id']:28} {s['type']:7} {s['name']}")
        return 0
    if a.utm:
        lat, lon = utm_to_latlon(float(a.utm[0]), float(a.utm[1]), int(a.utm[2]))
    elif a.coord:
        lat, lon = parse_coordinate(a.coord)
    else:
        ap.error("indicare una coordinata")
    res = run(Point(lat, lon), a.radius, a.sources_dir, a.only, timeout=a.timeout, geocode=not a.no_geocode, include_info=a.all)
    sys.stdout.write(to_json(res) if a.format == "json" else to_markdown(res))
    return 0
