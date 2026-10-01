"""
classificatore.py - Decide se un documento e' un preventivo EMESSO dal
professionista target (default: Per. Agr. Angelo Chiminelli).

Due punteggi indipendenti:
  * punti_preventivo : il documento e' un preventivo/offerta?
  * punti_autore     : l'EMITTENTE e' il target? (non basta che il nome compaia:
                       conta dove compare - intestazione/firma vs destinatario/D.L. -
                       e chi altro compare come mittente)

Ogni punto assegnato lascia una motivazione leggibile + un estratto di testo
con la pagina, cosi' la decisione e' verificabile e non una scatola nera.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from estrazione import Testo, normalizza

CONFIG_PREDEFINITA = {
    "nome": "Angelo",
    "cognome": "Chiminelli",
    # Dati identificativi reali del professionista (vanno inseriti nel file di
    # configurazione: lo script non li conosce). Vuoti = non usati.
    "identificativi": {
        "partita_iva": "",
        "codice_fiscale": "",
        "email": "",
        "pec": "",
        "telefono": "",
        "iscrizione_collegio": "",
    },
    # Diciture esatte della carta intestata (es. "studio tecnico ...") e indirizzo.
    "intestazione_esatta": [],
    # Localita'/indirizzo dello studio: indizio debole.
    "localita": [],
    # Ditte/professionisti che producono falsi positivi ricorrenti (regex, minuscolo).
    "emittenti_esclusi": [],
    # Righe ricorrenti apprese da preventivi certi (comando --impara). Non editare a mano.
    "impronta": [],
    # Frammenti cercati nel NOME del file (minuscolo, senza accenti).
    "parole_nome_file": ["preventiv", "offert", "quotazion", "computo", "proposta econ",
                         "parcell", "notul"],
    # Abbreviazioni cercate come parola isolata nel nome file (es. "prev_2023.pdf").
    "abbreviazioni_nome_file": ["prev", "off"],
    "finestra_caratteri": 800,     # inizio/fine documento = intestazione/firma
    "soglia_confermato": 9,
    "soglia_probabile": 5,
    "soglia_scartato": 0,          # punti_autore <= soglia -> SCARTATO
    "soglia_preventivo": 3,
}

ESITI = ["CONFERMATO", "PROBABILE", "DA_VERIFICARE", "SCARTATO", "NON_PREVENTIVO", "ERRORE"]

# Se precedono il nome (marcatore piu' vicino), il target NON e' l'emittente.
MARCATORI_NON_AUTORE = [
    r"spett", r"\begr", r"\bgent", r"\bc\.\s?a\.", r"cortese attenzione", r"all'?\s?att",
    r"\balla? sig", r"\bal per", r"destinatari", r"committente", r"\bcliente", r"per conto d",
    r"\brif\.", r"direzione (dei )?lavori", r"direttore (dei )?lavori", r"\bd\.\s?l\.",
    r"progettista", r"tecnico incaricato", r"per accettazione", r"inviat[oa] a",
    r"\bvs\.?\b", r"\ba:\s", r"richiesta (del|dal)", r"su richiesta",
]
# Se precedono il nome, il target e' l'autore/firmatario.
MARCATORI_AUTORE = [
    r"il tecnico", r"in fede", r"il professionista", r"timbro e firma", r"\bfirma\b",
    r"redatt[oa] da", r"studio tecnico", r"il perito", r"distinti saluti", r"cordiali saluti",
    r"il sottoscritto", r"\bmittente",
]
RE_NON_AUTORE = re.compile("|".join(MARCATORI_NON_AUTORE))
RE_AUTORE = re.compile("|".join(MARCATORI_AUTORE))

RE_TITOLO = re.compile(r"\bper\.?\s?agr\b\.?|perit[oi]\s+agrar|\bp\.\s?agr\.")
RE_SOCIETA = re.compile(
    r"\bs\.?\s?r\.?\s?l\b\.?|\bs\.\s?p\.\s?a\b\.?|\bspa\b|\bs\.?\s?n\.?\s?c\b\.?|\bs\.\s?a\.\s?s\b\.?"
    r"|soc\.?\s*coop|societa cooperativa|\bimpresa\b|\bditta\b")
# Nota: "Dott. Agr." / agronomo e' un ALTRO professionista, non un indizio a favore.
RE_ALTRI_PROF = re.compile(
    r"\bgeom\.|\bgeometra\b|\bing\.|\bingegner|\barch\.|\barchitett|\bdott\.?\s?(agr|for)"
    r"|\bagronom|\bavv\.|\bnotaio\b")
RE_PIVA = re.compile(
    r"(?:p\.?\s?iva|partita iva|c\.?\s?f\.?\s?/?\s?p\.?\s?iva)[\s:.n°/-]*(?:it)?\s?(\d{11})")
RE_IMPORTO = re.compile(
    r"(?:€|\beur(?:o)?\b)\s?(\d{1,3}(?:[.\s]\d{3})*(?:,\d{2})?|\d+(?:,\d{2})?)"
    r"|(\d{1,3}(?:[.\s]\d{3})*,\d{2}|\d+,\d{2})\s?(?:€|\beur(?:o)?\b)")
MESI = "gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre"
RE_DATA = re.compile(rf"\b(\d{{1,2}}[/.-]\d{{1,2}}[/.-](?:19|20)\d{{2}}|\d{{1,2}}\s(?:{MESI})\s(?:19|20)\d{{2}})\b")
RE_DOC_FISCALE = re.compile(
    r"\bfattura\s+(n|nr|num|numero)\b|documento di trasporto|\bd\.d\.t\.|nota di credito"
    r"|ordine d'?acquisto|conferma d'?ordine")

PAROLE_PREVENTIVO = [
    (r"\bpreventiv", 2, "'preventivo'"),
    (r"\bofferta\b", 2, "'offerta'"),
    (r"proposta economica|proposta di (incarico|parcella)|disciplinare d'incarico", 2,
     "'proposta economica/incarico'"),
    (r"computo metrico", 1, "computo metrico"),
    (r"onorari|compens[oi] professional|prestazion[ei] professional|spese tecniche", 1,
     "voci di onorario"),
    (RE_IMPORTO.pattern, 1, "importi in euro"),
    (r"\biva\b", 1, "IVA"),
    (r"\btotale\b|\bimponibile\b", 1, "totale/imponibile"),
    (r"validita|valid[oa] (per|fino)|per accettazione", 0.5, "validita'/accettazione"),
]
VOCI_PROFESSIONALI = re.compile(
    r"onorari|prestazion[ei] professional|competenze tecniche|spese tecniche"
    r"|contributo integrativo|cassa (di )?previdenza|enpaia|ritenuta d'acconto")
VOCI_FORNITURA = re.compile(
    r"posa in opera|manodopera|prezzo unitario|\bq\.?\s?ta\b|\bnoleggio\b|trasporto e scarico"
    r"|\bfornitura\b")
# Etichette per tipo di prestazione (solo parole chiave: indicative, non esaustive).
TIPI_PRESTAZIONE = {
    "Perizia/Stima": r"\bperizi|\bstima\b|\bstime\b|valutazione (economica|immobil|fondo)",
    "VTA/Alberature": r"\bv\.?t\.?a\.?\b|stabilita (degli |di )?alber|alberatur|abbattiment|potatur",
    "Catasto": r"accatastament|frazionament|tipo mappale|docfa|pregeo|catast|voltur",
    "Pratiche/Contributi": r"\bpsr\b|\bcsr\b|\bpac\b|domanda di (aiuto|contributo|pagamento)|bando|\bpua\b|\bpupa\b",
    "Progettazione": r"progettazion|progetto (del|di)|verde (pubblico|privato)",
    "Relazione/Consulenza": r"relazione (tecnica|agronomic|forestal)|consulenz",
    "Direzione lavori": r"direzione (dei )?lavori",
    "Rilievo/Topografia": r"rilievo|topografic|picchettament",
    "Successioni/Espropri": r"successi|espropri|servitu|indennit",
}


def _regex_cognome(cognome: str) -> str:
    """Tollerante a errori OCR (i/l/1) e a lettere spaziate (C H I M I ...)."""
    parti = ["[il1|!]" if c in "il" else re.escape(c) for c in normalizza(cognome)]
    return r"\s?".join(parti)


@dataclass
class Risultato:
    file: str
    formato: str = ""
    esito: str = ""
    punti_autore: float = 0.0
    punti_preventivo: float = 0.0
    tipo_documento: str = ""
    emittente_presunto: str = ""
    oggetto: str = ""
    importo: str = ""
    data: str = ""
    tipo_prestazione: str = ""
    firmatari: str = ""
    autore_metadati: str = ""
    evidenza: str = ""
    motivi: list[str] = field(default_factory=list)
    sha256: str = ""
    duplicato_di: str = ""


class Classificatore:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        cogn = _regex_cognome(cfg["cognome"])
        nome = re.escape(normalizza(cfg["nome"]))
        iniz = re.escape(normalizza(cfg["nome"])[:1])
        self.re_cognome = re.compile(cogn)
        self.re_completo = re.compile(
            rf"{nome}\W{{1,4}}{cogn}|{cogn}\W{{1,4}}{nome}|\b{iniz}\.\s?{cogn}")
        self.identificativi = {
            k: normalizza(str(v)).replace(" ", "")
            for k, v in cfg.get("identificativi", {}).items() if str(v).strip()}
        self.re_esclusi = [re.compile(normalizza(e)) for e in cfg.get("emittenti_esclusi", []) if e]

    # ---------------- nome file ----------------
    def nome_file_candidato(self, nome: str) -> bool:
        n = normalizza(nome)
        if any(p in n for p in self.cfg["parole_nome_file"]):
            return True
        return any(re.search(rf"(^|[^a-z]){re.escape(a)}([^a-z]|$)", n)
                   for a in self.cfg["abbreviazioni_nome_file"])

    # ---------------- utilita' ----------------
    @staticmethod
    def _estratto(testo: str, inizio: int, fine: int) -> str:
        pagina = testo.count("\f", 0, inizio) + 1
        s = testo[max(0, inizio - 50):fine + 50].replace("\f", " ")
        return f"p.{pagina}: \"...{s.strip()}...\""

    @staticmethod
    def _contesto(testo: str, pos: int) -> str:
        """'autore', 'non_autore' o '' secondo il marcatore piu' vicino prima di pos."""
        prima = testo[max(0, pos - 150):pos]
        ultimo_na = max((m.end() for m in RE_NON_AUTORE.finditer(prima)), default=-1)
        ultimo_a = max((m.end() for m in RE_AUTORE.finditer(prima)), default=-1)
        if ultimo_na < 0 and ultimo_a < 0:
            return ""
        return "autore" if ultimo_a > ultimo_na else "non_autore"

    @staticmethod
    def _nome_emittente(testo: str, m: re.Match) -> str:
        """'rossi costruzioni s.r.l.' (forma societaria in coda) oppure
        'geom. luca neri' / 'impresa verdi costruzioni' (qualifica in testa)."""
        if re.match(r"s\.?\s?[rpna]", m.group(0)):
            prima = re.split(r"[,;:]|\s-\s", testo[max(0, m.start() - 50):m.start()])[-1]
            return " ".join(prima.split()[-4:] + [m.group(0).strip()])
        dopo = re.split(r"[,;:]|\s-\s", testo[m.end():m.end() + 50])[0]
        return " ".join([m.group(0).strip()] + dopo.split()[:3])

    # ---------------- preventivo? ----------------
    def punteggio_preventivo(self, testo: str, regione: int) -> tuple[float, list[str], str]:
        punti, motivi = 0.0, []
        for rx, peso, descr in PAROLE_PREVENTIVO:
            if re.search(rx, testo):
                punti += peso
                motivi.append(descr)
        testa = testo[:regione]
        tipo = next((t for rx, t in ((r"\bpreventiv", "preventivo"), (r"\bofferta\b", "offerta"),
                                     (r"proposta (economica|di)", "proposta economica"),
                                     (r"\bparcella|\bnotula", "parcella"),
                                     (r"computo metrico", "computo metrico"))
                     if re.search(rx, testa)), "")
        fiscale = RE_DOC_FISCALE.search(testa)
        if fiscale and tipo not in ("preventivo", "offerta"):
            punti -= 3
            motivi.append(f"documento fiscale/ordine ('{fiscale.group(0)}')")
            tipo = tipo or "documento fiscale"
        return punti, motivi, tipo

    # ---------------- emittente = target? ----------------
    def punteggio_autore(self, testo: str, intest: str, firmatari: list[str], autore_meta: str):
        cfg = self.cfg
        punti, motivi, evid = 0.0, [], []
        lung = len(testo)
        fin = cfg["finestra_caratteri"]
        regione = fin if lung > 2 * fin else lung // 2 + 1

        def in_regione(pos):
            return pos < regione or pos > lung - regione

        # 1) Firmatario digitale (.p7m): il segnale piu' affidabile.
        for f in firmatari:
            if self.re_cognome.search(normalizza(f)):
                punti += 8
                motivi.append(f"firmato digitalmente da {f.strip()[:60]} (+8)")
            else:
                punti -= 4
                motivi.append(f"firmato digitalmente da altro soggetto: {f.strip()[:60]} (-4)")

        # 2) Intestazione / pie' di pagina del .docx (carta intestata).
        if intest and self.re_cognome.search(intest):
            punti += 5
            motivi.append("nome nell'intestazione/pie' di pagina (+5)")
            if RE_TITOLO.search(intest):
                punti += 2
                motivi.append("titolo Per. Agr. in intestazione (+2)")
        elif intest:
            soc = RE_SOCIETA.search(intest)
            if soc:
                punti -= 4
                motivi.append(f"intestazione docx di societa'/ditta ('{soc.group(0)}') (-4)")

        # 3) Occorrenze del nome nel testo, pesate per posizione e contesto.
        migliore, m_migliore, zone_destinatario = 0.0, None, []
        for m in self.re_cognome.finditer(testo):
            ctx = self._contesto(testo, m.start())
            vicino = testo[max(0, m.start() - 80):m.end() + 80]
            if ctx == "non_autore":
                zone_destinatario.append((m.start(), m.end() + 250))
                if not evid:
                    evid.append("destinatario: " + self._estratto(testo, m.start(), m.end()))
                continue
            if in_regione(m.start()) or ctx == "autore":
                v = (5 if self.re_completo.search(vicino) else 3) \
                    + (3 if RE_TITOLO.search(vicino) else 0) + (2 if ctx == "autore" else 0)
            else:
                v = 1                   # citato nel corpo: indizio debole
            if v > migliore:
                migliore, m_migliore = v, m
        if migliore:
            punti += migliore
            motivi.append(f"nome in posizione da emittente (+{migliore:g})" if migliore > 1
                          else "nome citato solo nel corpo del testo (+1)")
            evid.insert(0, self._estratto(testo, m_migliore.start(), m_migliore.end()))
        elif zone_destinatario:
            punti -= 3
            motivi.append("nome presente solo come destinatario/committente/D.L. (-3)")

        def fuori_destinatario(pos):
            return not any(a <= pos <= b for a, b in zone_destinatario)

        # 4) Identificativi, diciture esatte, impronta appresa, localita'.
        trovati = []
        for k, v in self.identificativi.items():
            rx = r"\s?".join(re.escape(c) for c in v)     # tollera spazi (es. telefono)
            if any(fuori_destinatario(mm.start()) for mm in re.finditer(rx, testo)):
                trovati.append(k)
        if intest:
            trovati += [k for k, v in self.identificativi.items()
                        if v in intest.replace(" ", "") and k not in trovati]
        if trovati:
            punti += min(8, 4 * len(trovati))
            motivi.append(f"identificativi del professionista: {', '.join(trovati)} "
                          f"(+{min(8, 4 * len(trovati))})")
        for nome_lista, peso, massimo in (("intestazione_esatta", 4, 8), ("impronta", 2, 6),
                                          ("localita", 1, 1)):
            voci = [normalizza(x) for x in cfg.get(nome_lista, []) if x.strip()]
            hit = [x for x in voci
                   if any(fuori_destinatario(mm.start())
                          for mm in re.finditer(re.escape(x), testo)) or x in intest]
            if hit:
                p = min(massimo, peso * len(hit))
                punti += p
                motivi.append(f"{nome_lista}: {len(hit)} riscontri (+{p:g})")
        if autore_meta and self.re_cognome.search(normalizza(autore_meta)):
            punti += 2
            motivi.append(f"autore nei metadati: {autore_meta[:50]} (+2)")

        piva_cfg = self.identificativi.get("partita_iva")
        if piva_cfg and "partita_iva" not in trovati:
            altre = {p for p in RE_PIVA.findall(testo + " " + intest) if p != piva_cfg}
            if altre:
                punti -= 2
                motivi.append("P.IVA di altri soggetti: " + ", ".join(sorted(altre)[:3]) + " (-2)")

        # 5) Mittente diverso nelle prime righe (ditta / altro professionista / escluso).
        testa = testo[:regione]
        emittente = ""
        for rx_list, peso, descr in (([*self.re_esclusi], 6, "emittente escluso"),
                                     ([RE_SOCIETA], 3, "societa'/ditta"),
                                     ([RE_ALTRI_PROF], 2, "altro professionista")):
            colpito = False
            for rx in rx_list:
                for m in rx.finditer(testa):
                    if self._contesto(testa, m.start()) == "non_autore":
                        continue        # e' il destinatario, non il mittente
                    if self.re_cognome.search(testa[max(0, m.start() - 60):m.end() + 60]):
                        continue
                    punti -= peso
                    motivi.append(f"intestazione di {descr} ('{m.group(0).strip()}') (-{peso})")
                    evid.append("mittente diverso: " + self._estratto(testa, m.start(), m.end()))
                    if not emittente:
                        emittente = self._nome_emittente(testa, m)
                    colpito = True
                    break
                if colpito:
                    break

        # 6) Natura delle voci.
        if VOCI_PROFESSIONALI.search(testo):
            punti += 1
            motivi.append("voci di prestazione professionale (+1)")
        elif VOCI_FORNITURA.search(testo):
            punti -= 1
            motivi.append("voci tipiche di fornitura/lavori di ditta (-1)")

        presente = (self.re_cognome.search(testo) or (intest and self.re_cognome.search(intest))
                    or any(self.re_cognome.search(normalizza(f)) for f in firmatari))
        if not presente and not trovati:
            punti -= 3
            motivi.append(f"il nome '{cfg['cognome']}' non compare (-3)")
        return punti, motivi, " || ".join(evid[:2]), emittente

    # ---------------- dati del preventivo ----------------
    @staticmethod
    def dati_preventivo(testo: str) -> dict:
        d = {}
        m = re.search(r"\boggetto\s*:?\s*(.{10,160}?)(?=\s(?:spett|egr|gent|premesso|con la presente"
                      r"|si (trasmette|invia)|in riferimento)|[.;]\s|$)", testo)
        d["oggetto"] = m.group(1).strip(" :-") if m else ""
        tot = re.search(r"\btotale\b[^€\d]{0,40}" + f"(?:{RE_IMPORTO.pattern})", testo)
        if tot:
            d["importo"] = next(g for g in tot.groups() if g)
        else:
            valori = []
            for m in RE_IMPORTO.finditer(testo):
                s = next(g for g in m.groups() if g)
                try:
                    valori.append((float(s.replace(".", "").replace(" ", "").replace(",", ".")), s))
                except ValueError:
                    pass
            d["importo"] = max(valori)[1] if valori else ""
        if d["importo"]:
            d["importo"] = "€ " + d["importo"]
        m = RE_DATA.search(testo)
        d["data"] = m.group(1) if m else ""
        d["tipo_prestazione"] = ", ".join(k for k, rx in TIPI_PRESTAZIONE.items()
                                          if re.search(rx, testo))
        return d

    # ---------------- decisione ----------------
    def classifica(self, nome_file: str, t: Testo, firmatari: list[str]) -> Risultato:
        cfg = self.cfg
        r = Risultato(file=nome_file, autore_metadati=t.autore)
        testo, intest = normalizza(t.corpo), normalizza(t.intestazione)
        regione = min(cfg["finestra_caratteri"], len(testo))
        r.punti_preventivo, motivi_p, r.tipo_documento = \
            self.punteggio_preventivo(intest + " " + testo, regione + len(intest))
        r.punti_autore, r.motivi, r.evidenza, emittente = \
            self.punteggio_autore(testo, intest, firmatari, t.autore)
        r.motivi += t.avvisi
        for k, v in self.dati_preventivo(testo).items():
            setattr(r, k, v)
        if r.punti_autore >= cfg["soglia_probabile"]:
            r.emittente_presunto = f"{cfg['nome']} {cfg['cognome']}"
        else:
            r.emittente_presunto = emittente

        if len(testo) < 80 and not firmatari:
            r.esito = "DA_VERIFICARE"
            r.motivi.insert(0, "testo insufficiente per decidere (scansione? usare --ocr)")
            return r
        if r.punti_preventivo < cfg["soglia_preventivo"]:
            if self.nome_file_candidato(nome_file) and r.punti_autore > cfg["soglia_scartato"]:
                r.esito = "DA_VERIFICARE"
                r.motivi.insert(0, "nome file da preventivo ma contenuto poco tipico (" +
                                (", ".join(motivi_p) or "nessun indizio") + ")")
            else:
                r.esito = "NON_PREVENTIVO"
                r.motivi.insert(0, "contenuto non da preventivo (" +
                                (", ".join(motivi_p) or "nessun indizio") + ")")
            return r
        if r.punti_autore >= cfg["soglia_confermato"]:
            r.esito = "CONFERMATO"
        elif r.punti_autore >= cfg["soglia_probabile"]:
            r.esito = "PROBABILE"
        elif r.punti_autore <= cfg["soglia_scartato"]:
            r.esito = "SCARTATO"
        else:
            r.esito = "DA_VERIFICARE"
        return r
