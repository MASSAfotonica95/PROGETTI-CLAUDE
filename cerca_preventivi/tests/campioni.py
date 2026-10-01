"""Generatore di documenti di prova (dati fittizi) per i test."""

from __future__ import annotations

import datetime
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

# ---------------------------------------------------------------- DOCX ----

_CT = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
{header}<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
</Types>"""
_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
</Relationships>"""
_DOCRELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rIdH" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>
</Relationships>"""
_W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" ' \
     'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'


def _par(righe):
    return "".join(f"<w:p><w:r><w:t xml:space=\"preserve\">{escape(r)}</w:t></w:r></w:p>"
                   for r in righe)


def scrivi_docx(percorso: Path, corpo: list[str], intestazione: list[str] | None = None,
                autore: str = ""):
    hdr_ref = '<w:headerReference w:type="default" r:id="rIdH"/>' if intestazione else ""
    doc = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {_W}><w:body>'
           f'{_par(corpo)}<w:sectPr>{hdr_ref}</w:sectPr></w:body></w:document>')
    core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/">'
            f'<dc:creator>{escape(autore)}</dc:creator></cp:coreProperties>')
    with zipfile.ZipFile(percorso, "w", zipfile.ZIP_DEFLATED) as z:
        ov = ('<Override PartName="/word/header1.xml" ContentType="application/'
              'vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>')
        z.writestr("[Content_Types].xml", _CT.replace("{header}", ov if intestazione else ""))
        z.writestr("_rels/.rels", _RELS)
        z.writestr("word/document.xml", doc)
        z.writestr("docProps/core.xml", core)
        z.writestr("word/_rels/document.xml.rels", _DOCRELS if intestazione else
                   _DOCRELS.split("<Relationship ")[0] + "</Relationships>")
        if intestazione:
            z.writestr("word/header1.xml",
                       f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:hdr {_W}>'
                       f'{_par(intestazione)}</w:hdr>')


# ----------------------------------------------------------------- PDF ----

def pdf_bytes(righe: list[str]) -> bytes:
    """PDF minimale valido, una pagina, font Helvetica (testo latin-1)."""
    def esc(s):
        return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    flusso = "BT /F1 11 Tf 14 TL 50 800 Td " + " ".join(f"({esc(r)}) Tj T*" for r in righe) + " ET"
    flusso_b = flusso.encode("latin-1")
    oggetti = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R "
        b"/Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length %d >>\nstream\n" % len(flusso_b) + flusso_b + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offs = []
    for i, o in enumerate(oggetti, 1):
        offs.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(oggetti) + 1)
    out += b"".join(b"%010d 00000 n \n" % o for o in offs)
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(oggetti) + 1, xref)
    return bytes(out)


# ----------------------------------------------------------------- P7M ----

def firma_p7m(contenuto: bytes, nome: str, cognome: str) -> bytes:
    """Busta CAdES/PKCS#7 'attached' DER con certificato autofirmato fittizio."""
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.serialization import pkcs7
    from cryptography.x509.oid import NameOID

    chiave = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    soggetto = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "IT"),
        x509.NameAttribute(NameOID.GIVEN_NAME, nome),
        x509.NameAttribute(NameOID.SURNAME, cognome),
        x509.NameAttribute(NameOID.COMMON_NAME, f"{cognome} {nome}".upper()),
    ])
    ora = datetime.datetime.now(datetime.timezone.utc)
    cert = (x509.CertificateBuilder().subject_name(soggetto).issuer_name(soggetto)
            .public_key(chiave.public_key()).serial_number(x509.random_serial_number())
            .not_valid_before(ora).not_valid_after(ora + datetime.timedelta(days=30))
            .sign(chiave, hashes.SHA256()))
    return (pkcs7.PKCS7SignatureBuilder().set_data(contenuto)
            .add_signer(cert, chiave, hashes.SHA256())
            .sign(serialization.Encoding.DER, [pkcs7.PKCS7Options.Binary]))


# ------------------------------------------------------------ CORPUS ----

CHIM_INTEST = ["Per. Agr. Angelo Chiminelli", "Studio Tecnico Agrario",
               "Via dei Campi 1 - 25000 Paese (XX)", "tel. 000 0000000 - info@esempio.it"]

CHIM_CORPO = [
    "Paese, 12/03/2024", "Spett.le Azienda Agricola Rossi S.r.l.", "Via Verdi 5 - Altro Paese",
    "Oggetto: preventivo per perizia di stima del fondo agricolo in localita' Prati.",
    "Con la presente si trasmette l'offerta per la prestazione professionale in oggetto.",
    "Onorario per sopralluogo, rilievo e relazione di stima: euro 1.000,00",
    "Contributo integrativo 4%: euro 40,00", "Imponibile euro 1.040,00",
    "IVA 22%: euro 228,80", "Totale euro 1.268,80",
    "Validita' dell'offerta: 60 giorni.", "Distinti saluti.", "In fede",
    "Per. Agr. Angelo Chiminelli",
]

DITTA_A_CHIM = [
    "ELETTRO BIANCHI S.r.l.", "Impianti elettrici civili e industriali - P.IVA 01234567890",
    "Spett.le Per. Agr. Angelo Chiminelli", "Via dei Campi 1 - Paese",
    "Offerta n. 45 del 03/05/2023", "Oggetto: fornitura e posa in opera impianto di irrigazione.",
    "Fornitura quadro elettrico, prezzo unitario euro 900,00", "Manodopera euro 600,00",
    "Totale imponibile euro 1.500,00 + IVA 22%", "Distinti saluti", "Elettro Bianchi S.r.l.",
]

DITTA_DL = [
    "IMPRESA VERDI COSTRUZIONI S.n.c.", "di Verdi Mario & C.",
    "PREVENTIVO n. 7/2022", "Committente: Comune di Paese",
    "Direzione lavori: Per. Agr. Angelo Chiminelli",
    "Oggetto: realizzazione recinzione area verde pubblico.",
    "Scavo e posa in opera di paletti in legno: euro 3.200,00",
    "Totale lavori euro 3.200,00 oltre IVA", "Il legale rappresentante - Mario Verdi",
]

GEOMETRA = [
    "Geom. Luca Neri", "Studio Tecnico Neri - via Roma 3",
    "Spett.le Sig. Bruno Gialli", "Oggetto: preventivo per pratica di accatastamento.",
    "Onorario per pratica DOCFA: euro 800,00 + IVA", "Totale euro 976,00",
    "Distinti saluti", "Geom. Luca Neri",
]

VIVAIO_FIRMATO = [
    "VIVAI FIORITI S.a.s.", "Spett.le Comune di Paese",
    "Offerta economica per fornitura piante ornamentali", "n. 50 aceri campestri euro 1.250,00",
    "Trasporto e scarico euro 150,00", "Totale euro 1.400,00 + IVA", "Vivai Fioriti S.a.s.",
]


def genera_corpus(cartella: Path, con_p7m: bool = True, con_doc: bool = True) -> dict[str, str]:
    """Crea i file di prova; ritorna {nome relativo: esito atteso}."""
    attesi = {}
    a = cartella / "2024" / "clienti"
    b = cartella / "2023" / "fornitori"
    a.mkdir(parents=True, exist_ok=True)
    b.mkdir(parents=True, exist_ok=True)

    scrivi_docx(a / "Preventivo Rossi.docx", CHIM_CORPO, CHIM_INTEST, "Angelo Chiminelli")
    attesi["2024/clienti/Preventivo Rossi.docx"] = "CONFERMATO"

    scrivi_docx(b / "offerta impianto.docx", DITTA_A_CHIM, None, "Ufficio tecnico")
    attesi["2023/fornitori/offerta impianto.docx"] = "SCARTATO"

    (b / "preventivo recinzione.pdf").write_bytes(pdf_bytes(DITTA_DL))
    attesi["2023/fornitori/preventivo recinzione.pdf"] = "SCARTATO"

    (b / "prev_geometra.pdf").write_bytes(pdf_bytes(GEOMETRA))
    attesi["2023/fornitori/prev_geometra.pdf"] = "SCARTATO"

    (a / "preventivo_stima.pdf").write_bytes(pdf_bytes(CHIM_INTEST + CHIM_CORPO))
    attesi["2024/clienti/preventivo_stima.pdf"] = "CONFERMATO"

    # Stesso contenuto in un'altra cartella: deve risultare duplicato.
    (b / "copia preventivo_stima.pdf").write_bytes(pdf_bytes(CHIM_INTEST + CHIM_CORPO))
    attesi["2023/fornitori/copia preventivo_stima.pdf"] = "CONFERMATO"

    # Nome non indicativo: trovato solo con --tutti.
    (a / "documento 15.pdf").write_bytes(pdf_bytes(CHIM_INTEST + CHIM_CORPO[:-2]))
    attesi["2024/clienti/documento 15.pdf"] = "CONFERMATO"

    # Lettera di Chiminelli col nome da preventivo ma che non e' un preventivo.
    (a / "preventivo - lettera accompagnamento.pdf").write_bytes(pdf_bytes(
        CHIM_INTEST + ["Spett.le Comune di Paese", "Si trasmette la relazione richiesta.",
                       "Distinti saluti", "Per. Agr. Angelo Chiminelli"]))
    attesi["2024/clienti/preventivo - lettera accompagnamento.pdf"] = "DA_VERIFICARE"

    if con_p7m:
        pdf = pdf_bytes(CHIM_CORPO[:3] + ["Oggetto: preventivo per relazione agronomica PSR."]
                        + CHIM_CORPO[4:-1] + ["Il tecnico", "Angelo Chiminelli"])
        (a / "offerta PSR.pdf.p7m").write_bytes(firma_p7m(pdf, "Angelo", "Chiminelli"))
        attesi["2024/clienti/offerta PSR.pdf.p7m"] = "CONFERMATO"

        (b / "offerta piante.pdf.p7m").write_bytes(
            firma_p7m(pdf_bytes(VIVAIO_FIRMATO), "Carla", "Fioriti"))
        attesi["2023/fornitori/offerta piante.pdf.p7m"] = "SCARTATO"

        # Fattura elettronica firmata: va ignorata (non e' un documento di interesse).
        (b / "IT01234567890_preventivo.xml.p7m").write_bytes(
            firma_p7m(b"<FatturaElettronica/>", "Carla", "Fioriti"))

    if con_doc and (shutil.which("soffice") or shutil.which("libreoffice")):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "offerta vecchia.docx"
            scrivi_docx(src, CHIM_INTEST + CHIM_CORPO, None, "Angelo Chiminelli")
            exe = shutil.which("soffice") or shutil.which("libreoffice")
            subprocess.run([exe, "--headless", "--convert-to", "doc", "--outdir", d, str(src)],
                           capture_output=True, timeout=180)
            if (Path(d) / "offerta vecchia.doc").exists():
                shutil.copy(Path(d) / "offerta vecchia.doc", a / "offerta vecchia.doc")
                attesi["2024/clienti/offerta vecchia.doc"] = "CONFERMATO"

    (cartella / "Thumbs.db").write_bytes(b"x")
    (a / "~$eventivo Rossi.docx").write_bytes(b"lock")
    return attesi


if __name__ == "__main__":
    import sys
    dest = Path(sys.argv[1] if len(sys.argv) > 1 else "archivio_di_prova")
    for k, v in genera_corpus(dest).items():
        print(f"{v:<14} {k}")
