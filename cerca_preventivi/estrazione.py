"""
estrazione.py - Apertura delle buste firmate .p7m ed estrazione del testo
da .pdf, .doc, .docx, .rtf (con intestazioni/pie' di pagina e metadati autore).

Solo libreria standard; usa strumenti esterni se presenti (pdftotext/pdfinfo,
antiword/catdoc/LibreOffice, tesseract) e i pacchetti pypdf / cryptography.
"""

from __future__ import annotations

import base64
import hashlib
import html
import io
import os
import re
import shutil
import subprocess
import tempfile
import unicodedata
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

ESTENSIONI_DOC = {".pdf", ".doc", ".docx", ".rtf"}

# --------------------------------------------------------------------------
# Utilita'
# --------------------------------------------------------------------------


def normalizza(testo: str) -> str:
    """Minuscolo, senza accenti, spazi compattati."""
    testo = unicodedata.normalize("NFKD", testo)
    testo = "".join(c for c in testo if not unicodedata.combining(c))
    testo = testo.lower()
    # Compatta gli spazi ma conserva \f (separatore di pagina, serve a citare la pagina)
    return re.sub(r"[ \t\r\n\v\u00a0]+", " ", testo).strip()


def _cerca_programma(*nomi: str) -> str | None:
    for n in nomi:
        p = shutil.which(n)
        if p:
            return p
    return None


def _esegui(cmd: list[str], timeout: int = 120) -> str | None:
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", errors="replace")


def formato_da_contenuto(dati: bytes) -> str | None:
    """Riconosce il formato reale dai primi byte (i nomi file a volte mentono)."""
    if dati.startswith(b"%PDF") or b"%PDF-" in dati[:1024]:
        return ".pdf"
    if dati.startswith(b"PK\x03\x04"):
        return ".docx"
    if dati.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        return ".doc"
    if dati.startswith(b"{\\rtf"):
        return ".rtf"
    return None


# --------------------------------------------------------------------------
# Busta firmata .p7m (CAdES / PKCS#7 SignedData) - parser DER/BER minimale
# --------------------------------------------------------------------------

OID_SIGNED_DATA = bytes.fromhex("2a864886f70d010702")


class ErroreP7M(Exception):
    pass


def _elemento(b: bytes, i: int):
    """Ritorna (tag, inizio_contenuto, fine_contenuto, prossimo) gestendo
    anche la lunghezza indefinita BER usata da alcuni software di firma."""
    if i >= len(b):
        raise ErroreP7M("struttura troncata")
    tag = b[i]
    j = i + 1
    if tag & 0x1F == 0x1F:          # tag multi-byte
        while b[j] & 0x80:
            j += 1
        j += 1
    lung = b[j]
    j += 1
    if lung == 0x80:                # lunghezza indefinita: fino a 00 00
        k = j
        while not (b[k] == 0 and b[k + 1] == 0):
            k = _elemento(b, k)[3]
        return tag, j, k, k + 2
    if lung & 0x80:
        n = lung & 0x7F
        lung = int.from_bytes(b[j:j + n], "big")
        j += n
    if j + lung > len(b):
        raise ErroreP7M("lunghezza oltre la fine del file")
    return tag, j, j + lung, j + lung


def _figli(b: bytes, inizio: int, fine: int):
    """Elementi figli come (tag, inizio_contenuto, fine_contenuto, prossimo, inizio_tlv)."""
    out, i = [], inizio
    while i < fine:
        el = _elemento(b, i)
        out.append((*el, i))
        i = el[3]
    return out


def _octet_string(b: bytes, el) -> bytes:
    tag, s, e = el[0], el[1], el[2]
    if tag == 0x04:
        return b[s:e]
    if tag == 0x24:                 # OCTET STRING costruita (a pezzi)
        return b"".join(_octet_string(b, c) for c in _figli(b, s, e))
    raise ErroreP7M("contenuto non OCTET STRING")


def _forse_base64(dati: bytes) -> bytes:
    testa = dati[:64].lstrip()
    if testa.startswith(b"-----BEGIN"):
        righe = [r for r in dati.splitlines() if r and not r.startswith(b"-----")]
        return base64.b64decode(b"".join(righe))
    if testa[:2] == b"MI":          # DER in base64 inizia con "MI"
        try:
            return base64.b64decode(b"".join(dati.split()), validate=True)
        except ValueError:
            pass
    return dati


def _apri_busta(dati: bytes) -> tuple[bytes, list[str]]:
    """Una singola busta SignedData -> (contenuto, firmatari)."""
    try:
        if not dati or dati[0] != 0x30:
            raise ErroreP7M("non e' una busta PKCS#7")
        tag, s, e, _ = _elemento(dati, 0)
        ci = _figli(dati, s, e)
        if ci[0][0] != 0x06 or dati[ci[0][1]:ci[0][2]] != OID_SIGNED_DATA:
            raise ErroreP7M("non e' una busta SignedData")
        sd = _figli(dati, ci[1][1], ci[1][2])[0]
        parti = _figli(dati, sd[1], sd[2])   # version, digestAlgs, encap, [0]certs...
        encap = _figli(dati, parti[2][1], parti[2][2])
        firmatari = []
        for p in parti[3:]:
            if p[0] == 0xA0:                 # [0] certificates
                for c in _figli(dati, p[1], p[2]):
                    firmatari.append(_nome_firmatario(dati[c[4]:c[3]]))
        if len(encap) < 2:
            raise ErroreP7M("firma 'detached': il documento non e' dentro la busta")
        return _octet_string(dati, _figli(dati, encap[1][1], encap[1][2])[0]), firmatari
    except IndexError:
        raise ErroreP7M("busta p7m troncata o malformata") from None


def apri_p7m(dati: bytes) -> tuple[bytes, list[str]]:
    """Estrae il documento originale e i firmatari (anche buste annidate .p7m.p7m)."""
    contenuto, firmatari = _apri_busta(_forse_base64(dati))
    for _ in range(4):
        try:
            contenuto, altri = _apri_busta(_forse_base64(contenuto))
        except ErroreP7M:
            break
        firmatari += altri
    return contenuto, [f for f in firmatari if f]


def _nome_firmatario(der_cert: bytes) -> str:
    try:
        from cryptography import x509
        from cryptography.x509.oid import NameOID

        cert = x509.load_der_x509_certificate(der_cert)
        cn = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        cognome = cert.subject.get_attributes_for_oid(NameOID.SURNAME)
        nome = cert.subject.get_attributes_for_oid(NameOID.GIVEN_NAME)
        parti = [a.value for a in nome + cognome] or [a.value for a in cn]
        return " ".join(str(p) for p in parti)
    except Exception:
        # Senza 'cryptography': stringhe leggibili del certificato (CN, ecc.)
        stringhe = re.findall(rb"[A-Za-z][A-Za-z '\.\-/]{3,}", der_cert)
        return " ".join(s.decode("latin-1") for s in stringhe[:40])




# --------------------------------------------------------------------------
# Estrazione testo
# --------------------------------------------------------------------------


@dataclass
class Testo:
    corpo: str = ""                 # testo completo; le pagine PDF sono separate da \f
    intestazione: str = ""          # intestazioni/pie' di pagina del .docx (carta intestata)
    autore: str = ""                # metadati: autore / ultimo a modificare
    avvisi: list[str] = field(default_factory=list)


def _xml_in_testo(xml: str) -> str:
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:(tab|br|cr)\b[^>]*/>", " ", xml)
    xml = re.sub(r"<[^>]+>", "", xml)
    return html.unescape(xml)


def testo_docx(dati: bytes) -> Testo:
    t = Testo()
    with zipfile.ZipFile(io.BytesIO(dati)) as z:
        nomi = z.namelist()
        if "word/document.xml" not in nomi:
            raise ValueError("archivio zip che non e' un documento Word (.docx)")
        leggi = lambda n: z.read(n).decode("utf-8", "replace")  # noqa: E731
        t.corpo = _xml_in_testo(leggi("word/document.xml"))
        hf = sorted(n for n in nomi if re.match(r"word/(header|footer)\d*\.xml$", n))
        t.intestazione = "\n".join(_xml_in_testo(leggi(n)) for n in hf)
        for n in ("word/footnotes.xml", "word/endnotes.xml"):
            if n in nomi:
                t.corpo += "\n" + _xml_in_testo(leggi(n))
        if "docProps/core.xml" in nomi:
            core = leggi("docProps/core.xml")
            autori = re.findall(r"<(?:dc:creator|cp:lastModifiedBy)>([^<]*)<", core)
            t.autore = " / ".join(dict.fromkeys(html.unescape(a) for a in autori if a.strip()))
    return t


def testo_pdf(percorso: Path, ocr: bool) -> Testo:
    t = Testo()
    exe = _cerca_programma("pdftotext")
    if exe:
        t.corpo = _esegui([exe, "-enc", "UTF-8", str(percorso), "-"]) or ""
        info = _esegui([_cerca_programma("pdfinfo") or "pdfinfo", str(percorso)]) or ""
        m = re.search(r"^Author:\s*(.+)$", info, re.M)
        t.autore = m.group(1).strip() if m else ""
    if not t.corpo.strip():
        try:
            from pypdf import PdfReader

            r = PdfReader(str(percorso))
            t.corpo = "\f".join((p.extract_text() or "") for p in r.pages)
            t.autore = t.autore or str((r.metadata or {}).get("/Author", "") or "")
        except ImportError:
            if not exe:
                t.avvisi.append("manca pdftotext/pypdf: impossibile leggere i PDF")
        except Exception as exc:
            t.avvisi.append(f"pypdf: {exc}")
    if len(normalizza(t.corpo)) < 80:
        if ocr:
            t.corpo = _ocr_pdf(percorso, t)
        else:
            t.avvisi.append("PDF quasi senza testo (scansione?): usare --ocr o verificare a mano")
    return t


def _ocr_pdf(percorso: Path, t: Testo) -> str:
    tess, ppm = _cerca_programma("tesseract"), _cerca_programma("pdftoppm")
    if not (tess and ppm):
        t.avvisi.append("OCR richiesto ma tesseract/pdftoppm non disponibili")
        return t.corpo
    with tempfile.TemporaryDirectory() as d:
        # Le prime 2 pagine bastano quasi sempre: intestazione, oggetto, importo.
        _esegui([ppm, "-r", "300", "-l", "2", "-png", str(percorso), os.path.join(d, "p")], 300)
        testi = []
        for img in sorted(Path(d).glob("p*.png")):
            out = _esegui([tess, str(img), "-", "-l", "ita"], 300) or \
                _esegui([tess, str(img), "-"], 300)
            testi.append(out or "")
    t.avvisi.append("testo ottenuto con OCR (prime 2 pagine)")
    return "\f".join(testi)


def testo_doc(percorso: Path, dati: bytes) -> Testo:
    t = Testo()
    for prog, args in (("antiword", ["-w", "0"]), ("catdoc", ["-w"])):
        exe = _cerca_programma(prog)
        if exe:
            out = _esegui([exe, *args, str(percorso)])
            if out and out.strip():
                t.corpo = out
                return t
    soffice = _cerca_programma("soffice", "libreoffice")
    if soffice:
        # Conversione in .docx: cosi' si recuperano anche intestazioni e autore.
        with tempfile.TemporaryDirectory() as d:
            _esegui([soffice, "--headless", "--convert-to", "docx", "--outdir", d,
                     str(percorso)], 180)
            out = list(Path(d).glob("*.docx"))
            if out:
                return testo_docx(out[0].read_bytes())
    # Ultima risorsa: stringhe leggibili dal binario Word 97-2003.
    t.avvisi.append("lettura .doc approssimata (installare antiword o LibreOffice)")
    utf16 = re.findall(rb"(?:[\x20-\x7e\xa0-\xff]\x00){4,}", dati)
    cp1252 = re.findall(rb"[\x20-\x7e\xa0-\xff\r\n\t]{6,}", dati)
    t.corpo = "\n".join([s.decode("utf-16-le", "replace") for s in utf16] +
                        [s.decode("cp1252", "replace") for s in cp1252])
    return t


def testo_rtf(dati: bytes) -> Testo:
    s = dati.decode("latin-1", "replace")
    s = re.sub(r"\\'([0-9a-fA-F]{2})",
               lambda m: bytes.fromhex(m.group(1)).decode("cp1252", "replace"), s)
    s = re.sub(r"\\par[d]?\b", "\n", s)
    s = re.sub(r"\\[a-zA-Z]+-?\d* ?|[{}]", "", s)
    return Testo(corpo=s)


def estrai_testo(formato: str, dati: bytes, ocr: bool = False) -> Testo:
    if formato == ".docx":
        return testo_docx(dati)
    if formato == ".rtf":
        return testo_rtf(dati)
    # pdf/doc: gli strumenti esterni vogliono un file su disco
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / f"documento{formato}"
        p.write_bytes(dati)
        return testo_pdf(p, ocr) if formato == ".pdf" else testo_doc(p, dati)


def formato_dichiarato(percorso: Path) -> tuple[str, bool]:
    """('.pdf', True) per 'x.pdf.p7m'; ('', True) per 'x.p7m' senza estensione interna."""
    suff = [s.lower() for s in percorso.suffixes]
    firmato = False
    while suff and suff[-1] == ".p7m":
        suff.pop()
        firmato = True
    interno = suff[-1] if suff else ""
    return (interno if interno in ESTENSIONI_DOC else ""), firmato


@dataclass
class Documento:
    """Contenuto 'aperto' di un file: formato reale, testo, firmatari, hash del contenuto."""
    formato: str
    testo: Testo
    firmatari: list[str]
    sha256: str


def apri_documento(percorso: Path, ocr: bool = False) -> Documento | None:
    """None se il file non e' un documento di interesse (es. fattura .xml.p7m)."""
    dichiarato, firmato = formato_dichiarato(percorso)
    if not dichiarato and not firmato:
        return None
    dati = percorso.read_bytes()
    firmatari: list[str] = []
    if firmato:
        dati, firmatari = apri_p7m(dati)
    formato = formato_da_contenuto(dati) or dichiarato
    if formato not in ESTENSIONI_DOC:
        return None
    t = estrai_testo(formato, dati, ocr)
    # Hash del contenuto interno: x.pdf e x.pdf.p7m risultano duplicati.
    return Documento(formato + (".p7m" if firmato else ""), t, firmatari,
                     hashlib.sha256(dati).hexdigest())
