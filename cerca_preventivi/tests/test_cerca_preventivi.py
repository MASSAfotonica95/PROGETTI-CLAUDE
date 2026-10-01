"""Test: python -m unittest discover -s tests   (dalla cartella cerca_preventivi)"""

import base64
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

QUI = Path(__file__).resolve().parent
sys.path[:0] = [str(QUI.parent), str(QUI)]

import cerca_preventivi as cp  # noqa: E402
import estrazione  # noqa: E402
from campioni import (CHIM_CORPO, CHIM_INTEST, DITTA_A_CHIM, genera_corpus,  # noqa: E402
                      pdf_bytes, scrivi_docx)
from classificatore import CONFIG_PREDEFINITA  # noqa: E402

HA_CRYPTO = importlib.util.find_spec("cryptography") is not None

if HA_CRYPTO:
    from campioni import firma_p7m


def cfg(**extra):
    c = json.loads(json.dumps(CONFIG_PREDEFINITA))
    c.update(extra)
    return c


class TestCorpus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.radice = Path(cls.tmp.name) / "archivio"
        cls.attesi = genera_corpus(cls.radice, con_p7m=HA_CRYPTO)
        cls.ris = {Path(r.file).relative_to(cls.radice).as_posix(): r
                   for r in cp.scansiona([cls.radice], cfg(), tutti=True)}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_esiti_attesi(self):
        for nome, esito in self.attesi.items():
            with self.subTest(nome):
                r = self.ris[nome]
                self.assertEqual(r.esito, esito, f"{nome}: {r.punti_autore} {r.motivi}")

    def test_file_non_pertinenti_ignorati(self):
        self.assertFalse(any("xml.p7m" in n or "~$" in n or "Thumbs" in n for n in self.ris))

    def test_duplicati(self):
        dup = [r for r in self.ris.values() if r.duplicato_di]
        self.assertEqual(len(dup), 1)
        self.assertIn("preventivo_stima.pdf", dup[0].file)

    def test_filtro_nome(self):
        nomi = [Path(r.file).name for r in cp.scansiona([self.radice], cfg())]
        self.assertNotIn("documento 15.pdf", nomi)
        self.assertIn("Preventivo Rossi.docx", nomi)

    def test_dati_estratti(self):
        r = self.ris["2024/clienti/Preventivo Rossi.docx"]
        self.assertEqual(r.importo, "€ 1.268,80")
        self.assertEqual(r.data, "12/03/2024")
        self.assertIn("perizia di stima", r.oggetto)
        self.assertIn("Perizia/Stima", r.tipo_prestazione)
        self.assertIn("chiminelli", r.evidenza)
        r = self.ris["2023/fornitori/offerta impianto.docx"]
        self.assertIn("bianchi s.r.l.", r.emittente_presunto)
        self.assertIn("destinatario", r.evidenza)

    @unittest.skipUnless(HA_CRYPTO, "serve 'cryptography' per creare i .p7m")
    def test_firmatario(self):
        self.assertIn("Chiminelli", self.ris["2024/clienti/offerta PSR.pdf.p7m"].firmatari)

    def test_report_e_copia(self):
        risultati = list(self.ris.values())
        out = Path(self.tmp.name) / "report.csv"
        cp.scrivi_report(risultati, out)
        testo = out.read_text("utf-8-sig")
        self.assertTrue(testo.startswith("esito;punti_autore"))
        self.assertTrue(out.with_suffix(".json").exists())
        dest = Path(self.tmp.name) / "copie"
        cp.copia_risultati(risultati, [self.radice], dest, {"CONFERMATO"})
        self.assertTrue((dest / "01_CONFERMATO/2024/clienti/Preventivo Rossi.docx").exists())
        self.assertFalse(list(dest.rglob("offerta impianto.docx")))


@unittest.skipUnless(HA_CRYPTO, "serve 'cryptography' per creare i .p7m")
class TestP7M(unittest.TestCase):
    def test_base64_e_annidato(self):
        pdf = pdf_bytes(["prova"])
        busta = firma_p7m(firma_p7m(pdf, "Angelo", "Chiminelli"), "Mario", "Rossi")
        pem = b"-----BEGIN PKCS7-----\n" + base64.encodebytes(busta) + b"-----END PKCS7-----\n"
        for dati in (busta, base64.b64encode(busta), pem):
            contenuto, firmatari = estrazione.apri_p7m(dati)
            self.assertEqual(contenuto, pdf)
            self.assertEqual(sorted(firmatari), ["Angelo Chiminelli", "Mario Rossi"])

    def test_p7m_rovinato(self):
        with self.assertRaises(estrazione.ErroreP7M):
            estrazione.apri_p7m(firma_p7m(b"x" * 500, "A", "B")[:200])


class TestEstrazione(unittest.TestCase):
    def test_docx_intestazione_e_autore(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "x.docx"
            scrivi_docx(p, ["corpo"], ["Per. Agr. Angelo Chiminelli"], "A. Chiminelli")
            t = estrazione.testo_docx(p.read_bytes())
        self.assertIn("Chiminelli", t.intestazione)
        self.assertEqual(t.autore, "A. Chiminelli")

    def test_doc_ripiego_senza_programmi(self):
        testo = "Per. Agr. Angelo Chiminelli - preventivo onorario"
        dati = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1" + b"\x00" * 600 + testo.encode("utf-16-le")
        with mock.patch.object(estrazione, "_cerca_programma", return_value=None):
            t = estrazione.estrai_testo(".doc", dati)
        self.assertIn(testo, t.corpo)
        self.assertTrue(t.avvisi)

    def test_formato_dichiarato(self):
        self.assertEqual(estrazione.formato_dichiarato(Path("a.PDF.p7m")), (".pdf", True))
        self.assertEqual(estrazione.formato_dichiarato(Path("a.p7m.p7m")), ("", True))
        self.assertEqual(estrazione.formato_dichiarato(Path("a.xml.p7m")), ("", True))
        self.assertEqual(estrazione.formato_dichiarato(Path("a.txt")), ("", False))


class TestClassificazione(unittest.TestCase):
    def _classifica(self, righe, **c):
        clf = cp.Classificatore(cfg(**c))
        return clf.classifica("preventivo.pdf", estrazione.Testo(corpo="\n".join(righe)), [])

    def test_identificativi(self):
        ident = {"email": "info@esempio.it", "partita_iva": "09876543210"}
        r = self._classifica(CHIM_INTEST + CHIM_CORPO, identificativi=ident)
        self.assertIn("email", " ".join(r.motivi))
        # L'email di Chiminelli nel blocco destinatario di una ditta NON conta.
        righe = DITTA_A_CHIM[:3] + ["info@esempio.it"] + DITTA_A_CHIM[3:]
        r = self._classifica(righe, identificativi=ident)
        self.assertEqual(r.esito, "SCARTATO")
        self.assertNotIn("identificativi", " ".join(r.motivi))
        self.assertIn("P.IVA di altri", " ".join(r.motivi))

    def test_emittente_escluso(self):
        righe = ["Studio Agronomico Esempio", "Preventivo per consulenza",
                 "Per. Agr. Angelo Chiminelli in collaborazione",
                 "Onorario euro 500,00 + IVA, totale euro 610,00"]
        r = self._classifica(righe, emittenti_esclusi=["studio agronomico esempio"])
        self.assertIn("emittente escluso", " ".join(r.motivi))

    def test_ocr_tollerante(self):
        r = self._classifica(["Per. Agr. Angelo Chlmine1li", *CHIM_CORPO[2:-1], "Per. Agr. A. Chimine11i"])
        self.assertIn(r.esito, ("CONFERMATO", "PROBABILE"))


class TestImparaECache(unittest.TestCase):
    def test_impara(self):
        with tempfile.TemporaryDirectory() as d:
            es = Path(d) / "esempi"
            es.mkdir()
            for i in range(3):
                (es / f"p{i}.pdf").write_bytes(pdf_bytes(
                    CHIM_INTEST + [f"Spett.le Cliente numero {i}"] + CHIM_CORPO[3:]))
            conf = Path(d) / "config.json"
            impronta = cp.impara([es], conf, ocr=False)
            self.assertIn("studio tecnico agrario", impronta)
            self.assertNotIn("spett.le cliente numero 1", impronta)
            self.assertEqual(json.loads(conf.read_text("utf-8"))["impronta"], impronta)
            self.assertEqual(cp.carica_config(str(conf))["impronta"], impronta)

    def test_cache_incrementale(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "preventivo.pdf").write_bytes(pdf_bytes(CHIM_INTEST + CHIM_CORPO))
            db = Path(d) / "indice.sqlite"
            primo = cp.scansiona([Path(d)], cfg(), cache_path=db)
            with mock.patch.object(cp, "apri_documento", side_effect=AssertionError("riletto")):
                secondo = cp.scansiona([Path(d)], cfg(), cache_path=db)
            self.assertEqual([r.esito for r in primo], [r.esito for r in secondo])
            self.assertEqual(primo[0].esito, "CONFERMATO")


if __name__ == "__main__":
    unittest.main()
