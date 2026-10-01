#!/usr/bin/env python3
"""
cerca_preventivi.py - Trova, in intere cartelle, i preventivi EMESSI dal
Per. Agr. Angelo Chiminelli, scartando quelli di altre ditte/professionisti.

Pipeline:
  1. scansione ricorsiva (.pdf, .doc, .docx, .rtf e i relativi .p7m firmati)
  2. selezione per nome file (preventivo, offerta, prev, computo, ...) - disattivabile con --tutti
  3. apertura busta .p7m (con nome del firmatario) ed estrazione testo/metadati
  4. punteggio "e' un preventivo?" + punteggio "l'emittente e' Chiminelli?"
  5. esito CONFERMATO / PROBABILE / DA_VERIFICARE / SCARTATO / NON_PREVENTIVO / ERRORE,
     con motivazioni ed estratto di testo; report CSV (Excel) + JSON

L'archivio originale non viene mai modificato (--copia crea solo copie).

Esempi:
  python cerca_preventivi.py "D:\\Archivio" -c config.json
  python cerca_preventivi.py "D:\\Archivio" -c config.json --tutti --ocr --cache indice.sqlite
  python cerca_preventivi.py --impara "D:\\Esempi_certi" -c config.json
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import sqlite3
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from classificatore import CONFIG_PREDEFINITA, ESITI, Classificatore, Risultato  # noqa: E402
from estrazione import (Documento, Testo, apri_documento, formato_dichiarato,  # noqa: E402
                        normalizza)

# --------------------------------------------------------------------------
# Configurazione
# --------------------------------------------------------------------------


def carica_config(percorso: str | None) -> dict:
    cfg = json.loads(json.dumps(CONFIG_PREDEFINITA))
    if percorso and Path(percorso).exists():
        utente = json.loads(Path(percorso).read_text("utf-8"))
        utente = {k: v for k, v in utente.items() if not k.startswith("_")}   # commenti
        ident = {**cfg["identificativi"], **utente.pop("identificativi", {})}
        cfg.update(utente)
        cfg["identificativi"] = ident
    return cfg


# --------------------------------------------------------------------------
# Cache SQLite: i file gia' letti e non modificati non vengono riaperti.
# Si memorizza il testo estratto (non l'esito), quindi cambiando configurazione
# la riclassificazione e' immediata.
# --------------------------------------------------------------------------


class Cache:
    def __init__(self, percorso: Path | None):
        self.db = None
        if percorso:
            self.db = sqlite3.connect(str(percorso))
            self.db.execute("""CREATE TABLE IF NOT EXISTS documenti (
                percorso TEXT PRIMARY KEY, dimensione INTEGER, mtime REAL, ocr INTEGER,
                dati TEXT)""")

    def leggi(self, p: Path, ocr: bool):
        if not self.db:
            return False, None
        st = p.stat()
        riga = self.db.execute(
            "SELECT dati FROM documenti WHERE percorso=? AND dimensione=? AND mtime=? AND ocr>=?",
            (str(p.resolve()), st.st_size, st.st_mtime, int(ocr))).fetchone()
        if riga is None:
            return False, None
        if riga[0] is None:
            return True, None           # file gia' visto, non di interesse
        d = json.loads(riga[0])
        return True, Documento(d["formato"], Testo(**d["testo"]), d["firmatari"], d["sha256"])

    def scrivi(self, p: Path, ocr: bool, doc: Documento | None):
        if not self.db:
            return
        st = p.stat()
        self.db.execute("INSERT OR REPLACE INTO documenti VALUES (?,?,?,?,?)",
                        (str(p.resolve()), st.st_size, st.st_mtime, int(ocr),
                         json.dumps(asdict(doc), ensure_ascii=False) if doc else None))

    def chiudi(self):
        if self.db:
            self.db.commit()
            self.db.close()


# --------------------------------------------------------------------------
# Scansione
# --------------------------------------------------------------------------


def elenca_file(radici: list[Path]):
    for radice in radici:
        if radice.is_file():
            yield radice
            continue
        for cartella, sottodir, files in os.walk(radice):
            sottodir[:] = sorted(d for d in sottodir if not d.startswith("."))
            for f in sorted(files):
                if f.startswith("~$") or f.startswith("."):
                    continue            # file di blocco di Word / nascosti
                yield Path(cartella) / f


def analizza_file(p: Path, clf: Classificatore, ocr: bool, cache: Cache) -> Risultato | None:
    dichiarato, firmato = formato_dichiarato(p)
    if not dichiarato and not firmato:
        return None
    try:
        trovato, doc = cache.leggi(p, ocr)
        if not trovato:
            doc = apri_documento(p, ocr)
            cache.scrivi(p, ocr, doc)
    except Exception as exc:
        return Risultato(file=str(p), esito="ERRORE", formato=dichiarato,
                         motivi=[f"{type(exc).__name__}: {exc}"])
    if doc is None:
        return None                     # es. fattura elettronica .xml.p7m
    r = clf.classifica(p.name, doc.testo, doc.firmatari)
    r.file, r.formato, r.sha256 = str(p), doc.formato, doc.sha256
    r.firmatari = "; ".join(f.strip()[:80] for f in doc.firmatari)
    return r


def scansiona(cartelle: list[Path], cfg: dict, tutti=False, ocr=False, cache_path=None,
              avanzamento=None) -> list[Risultato]:
    clf = Classificatore(cfg)
    cache = Cache(cache_path)
    risultati, visti = [], {}
    try:
        for p in elenca_file(cartelle):
            if not tutti and not clf.nome_file_candidato(p.name):
                continue
            r = analizza_file(p, clf, ocr, cache)
            if r is None:
                continue
            if r.sha256 in visti:
                r.duplicato_di = visti[r.sha256]
            elif r.sha256:
                visti[r.sha256] = r.file
            risultati.append(r)
            if avanzamento:
                avanzamento(r)
    finally:
        cache.chiudi()
    ordine = {e: i for i, e in enumerate(ESITI)}
    risultati.sort(key=lambda r: (ordine.get(r.esito, 9), -r.punti_autore, r.file))
    return risultati


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

COLONNE = ["esito", "punti_autore", "punti_preventivo", "file", "formato", "tipo_documento",
           "emittente_presunto", "oggetto", "importo", "data", "tipo_prestazione", "firmatari",
           "autore_metadati", "evidenza", "motivi", "duplicato_di", "sha256"]


def scrivi_report(risultati: list[Risultato], percorso: Path):
    with open(percorso, "w", newline="", encoding="utf-8-sig") as f:   # apribile da Excel
        w = csv.writer(f, delimiter=";")
        w.writerow(COLONNE)
        for r in risultati:
            d = asdict(r)
            d["motivi"] = " | ".join(r.motivi)
            d["punti_autore"], d["punti_preventivo"] = f"{r.punti_autore:g}", f"{r.punti_preventivo:g}"
            w.writerow([d[c] for c in COLONNE])
    percorso.with_suffix(".json").write_text(
        json.dumps([asdict(r) for r in risultati], ensure_ascii=False, indent=1), "utf-8")


def copia_risultati(risultati: list[Risultato], cartelle: list[Path], dest: Path, esiti: set[str]):
    for i, r in enumerate(risultati):
        if r.esito not in esiti or r.duplicato_di:
            continue
        src = Path(r.file).resolve()
        base = next((c.resolve() for c in cartelle
                     if c.is_dir() and src.is_relative_to(c.resolve())), src.parent)
        cartella = f"{ESITI.index(r.esito) + 1:02d}_{r.esito}"
        target = dest / cartella / src.relative_to(base)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)


def riepilogo(risultati: list[Risultato]) -> str:
    conta = {e: sum(r.esito == e for r in risultati) for e in ESITI}
    dup = sum(bool(r.duplicato_di) for r in risultati)
    return ", ".join(f"{k}={v}" for k, v in conta.items() if v) + (f" (duplicati: {dup})" if dup else "")


# --------------------------------------------------------------------------
# Apprendimento dell'impronta da preventivi certi
# --------------------------------------------------------------------------

GENERICHE = re.compile(
    r"preventiv|offerta|oggetto|spett|egr\.|gent|saluti|in fede|\btotale|\biva\b|imponibile"
    r"|\bpag(ina)?\.?\s?\d|\beuro\b|€|^\W*$|" + r"\b\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}\b")


def impara(esempi: list[Path], cfg_path: Path, ocr: bool) -> list[str]:
    """Righe di intestazione/firma che ricorrono in almeno meta' dei preventivi certi."""
    conteggio: dict[str, int] = {}
    n = 0
    for p in elenca_file(esempi):
        try:
            doc = apri_documento(p, ocr)
        except Exception as exc:
            print(f"  ignorato {p.name}: {exc}", file=sys.stderr)
            continue
        if doc is None:
            continue
        n += 1
        righe = [x for x in doc.testo.corpo.replace("\f", "\n").splitlines() if x.strip()]
        candidati = righe[:25] + righe[-25:] + doc.testo.intestazione.splitlines()
        pezzi = set()
        for riga in candidati:
            for pezzo in re.split(r"\s{3,}|\t|\s[-|•]\s", riga):    # colonne affiancate
                pezzo = normalizza(pezzo).strip(" .,;:-")
                if 10 <= len(pezzo) <= 90 and not GENERICHE.search(pezzo):
                    pezzi.add(pezzo)
        for pezzo in pezzi:
            conteggio[pezzo] = conteggio.get(pezzo, 0) + 1
    if n < 2:
        raise SystemExit("Servono almeno 2 preventivi certi per imparare l'impronta.")
    soglia = max(2, (n + 1) // 2)
    impronta = sorted(k for k, v in conteggio.items() if v >= soglia)
    cfg = json.loads(cfg_path.read_text("utf-8")) if cfg_path.exists() else {}
    cfg["impronta"] = impronta
    cfg_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), "utf-8")
    print(f"Analizzati {n} esempi; {len(impronta)} righe ricorrenti salvate in {cfg_path}:")
    for k in impronta:
        print(f"  - {k}")
    print("Controllare l'elenco e togliere righe non specifiche dello studio.")
    return impronta


# --------------------------------------------------------------------------


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Trova i preventivi emessi dal Per. Agr. Angelo Chiminelli.")
    ap.add_argument("cartelle", nargs="*", type=Path, help="cartelle (o file) da analizzare")
    ap.add_argument("-o", "--report", type=Path, default=Path("report_preventivi.csv"),
                    help="CSV di output (crea anche il .json accanto)")
    ap.add_argument("-c", "--config", type=Path, help="configurazione JSON (identificativi, soglie)")
    ap.add_argument("--tutti", action="store_true",
                    help="analizza il contenuto di TUTTI i file, non solo quelli col nome da preventivo")
    ap.add_argument("--ocr", action="store_true", help="OCR dei PDF scansionati (tesseract)")
    ap.add_argument("--cache", type=Path, help="indice SQLite per scansioni incrementali")
    ap.add_argument("--copia", type=Path,
                    help="copia qui i CONFERMATI/PROBABILI in sottocartelle per esito")
    ap.add_argument("--copia-anche-dubbi", action="store_true", help="con --copia, anche DA_VERIFICARE")
    ap.add_argument("--impara", nargs="+", type=Path, metavar="ESEMPI",
                    help="cartelle/file di preventivi CERTI: salva l'impronta nel file --config")
    ap.add_argument("-v", "--verbose", action="store_true", help="stampa l'esito di ogni file")
    a = ap.parse_args(argv)

    if a.impara:
        if not a.config:
            ap.error("--impara richiede -c/--config (dove salvare l'impronta)")
        impara(a.impara, a.config, a.ocr)
        return 0
    if not a.cartelle:
        ap.error("indicare almeno una cartella")

    def stampa(r):
        if a.verbose:
            print(f"[{r.esito:<14}] {r.punti_autore:>5g}  {r.file}", file=sys.stderr)

    risultati = scansiona(a.cartelle, carica_config(a.config), a.tutti, a.ocr, a.cache, stampa)
    scrivi_report(risultati, a.report)
    if a.copia:
        esiti = {"CONFERMATO", "PROBABILE"} | ({"DA_VERIFICARE"} if a.copia_anche_dubbi else set())
        copia_risultati(risultati, a.cartelle, a.copia, esiti)
    print(f"Riepilogo: {riepilogo(risultati) or 'nessun file trovato'}  ->  report: {a.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
