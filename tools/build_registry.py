"""Genera vincoli/sources/lombardia.json e brescia.json dai metadati reali dei servizi ArcGIS.

    python tools/build_registry.py            # rigenera entrambi (serve rete)

Per ogni livello: scarta i layer-gruppo, legge tipo di geometria e campi, sceglie i campi da mostrare,
individua campi data e campi-link. Il giudizio umano sta in SPEC (tema, norma, quali livelli, "info").
"""
from __future__ import annotations

import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

OUT = Path(__file__).resolve().parents[1] / "vincoli" / "sources"
S = requests.Session()
S.headers["User-Agent"] = "vincoli-territoriali/0.1 (build registro)"

A1 = "https://www.cartografia.servizirl.it/arcgis/rest/services"
A1B = "https://www.cartografia.servizirl.it/arcgis1/rest/services"
A2 = "https://www.cartografia.servizirl.it/arcgis2/rest/services"
BS = "https://sit.provincia.brescia.it/arcgis/rest/services"

LOMB = [8.4, 44.6, 11.5, 46.7]
BRESCIA = [9.75, 45.2, 10.95, 46.4]
C42 = "D.Lgs. 42/2004"

# (id, nome, base, servizio, livelli, opzioni)
# livelli: lista di id oppure "leaf" (tutti i livelli foglia); opzioni: theme, legal_ref, exclude (regex nome), info (True = livello
# informativo/di contesto, non un vincolo: incluso solo con --all), prox (metri per livelli lineari/puntuali), note
LOMBARDIA = [
    ("lom_siba_paesaggio", "Regione Lombardia – Vincoli paesaggistici (SIBA)", A2, "sistemiverdi/vincoli_paesaggistici",
     [14, 3, 0, 13, 2, 4, 5, 6, 7, 1, 10, 11, 8, 9, 12],
     dict(theme="paesaggistico", legal_ref=C42 + " artt. 136 e 142", note="Ricognitivo: verificare decreto/GU e cartografia originale.")),
    ("lom_ppr", "Regione Lombardia – Piano Paesaggistico Regionale (PPR)", A2, "sistemiverdi/piano_paesaggistico", "leaf",
     dict(theme="paesaggistico", legal_ref="PPR Lombardia (norme di attuazione)", exclude=r"^PPR art", note="Cartografia del PPR: prescrizioni da verificare nelle NdA.")),
    ("lom_ppr_indirizzi", "Regione Lombardia – Paesaggio: unità tipologiche", A2, "sistemiverdi/paesaggio_indirizzi", [7, 8],
     dict(theme="paesaggistico", legal_ref="PPR Lombardia", info=True)),
    ("lom_aree_protette", "Regione Lombardia – Aree protette", A2, "ambiente/AreeProtette", [1, 2, 4, 5, 6, 8, 9, 10, 11],
     dict(theme="ambientale", legal_ref="L. 394/1991; L.R. 86/1983; PLIS: L.R. 86/1983 art. 34", note="Dato regionale; verificare l'atto istitutivo.")),
    ("lom_natura2000", "Regione Lombardia – Rete Natura 2000", A2, "ambiente/Rete_Natura_2000", [0, 1, 2],
     dict(theme="ambientale", legal_ref="Dir. 92/43/CEE; Dir. 2009/147/CE; DPR 357/1997 (Valutazione di Incidenza)")),
    ("lom_rer", "Regione Lombardia – Rete Ecologica Regionale", A2, "sistemiverdi/rete_ecologica_regionale", [2, 3],
     dict(theme="ambientale", legal_ref="DGR 8/10962/2009 (RER)", info=True)),
    ("lom_pai", "Regione Lombardia – PAI vigente (dissesti e fasce fluviali)", A1B, "territorio/pai_vigente", "leaf",
     dict(theme="idrogeologico", legal_ref="PAI – L. 183/1989; Norme di Attuazione PAI (artt. 9, 29, 30, 31, 39)", exclude=r"^(Dissesti PAI vigenti|Fasce Fluviali vigenti)$",
          prox=25, note="Per le fasce fluviali fa fede il PAI vigente dell'Autorità di bacino.")),
    ("lom_iffi", "Regione Lombardia – Inventario fenomeni franosi (IFFI)", A1B, "protciv/iffi", "leaf",
     dict(theme="idrogeologico", legal_ref="Progetto IFFI (ISPRA/Regioni)", prox=25)),
    ("lom_pgra", "Regione Lombardia – PGRA aree allagabili (attestato del territorio)", A2, "protciv/attestato_territorio_master", [4, 5, 6, 7],
     dict(theme="idraulico", legal_ref="Dir. 2007/60/CE; D.Lgs. 49/2010 (PGRA)", note="Verificare l'ultima versione del PGRA (AdBPo).")),
    ("lom_attestato", "Regione Lombardia – Attestato del territorio (vincolo idrogeologico, difesa del suolo)", A2, "protciv/attestato_territorio_master",
     [29, 26, 27, 28, 37, 38],
     dict(theme="idrogeologico", legal_ref="R.D. 3267/1923 e L.R. 31/2008 (vincolo idrogeologico); DGR 3723/2015 (ambiti)")),
    ("lom_acquiferi", "Regione Lombardia – Vulnerabilità intrinseca degli acquiferi", A2, "protciv/attestato_territorio_master", [63],
     dict(theme="acque", legal_ref="D.Lgs. 152/2006 (tutela acque sotterranee)", info=True)),
    ("lom_attestato_info", "Regione Lombardia – Attestato del territorio (contesto)", A2, "protciv/attestato_territorio_master",
     [3, 71, 67, 68, 69, 70, 57],
     dict(theme="contesto", legal_ref="", info=True)),
    ("lom_zone_sismiche", "Regione Lombardia – Classificazione sismica dei comuni", A1B, "protciv/classificazione_sismica", [0],
     dict(theme="sismico", legal_ref="OPCM 3274/2003; D.G.R. Lombardia X/2129/2014", note="Classificazione vigente: fa fede l'ultimo atto regionale.")),
    ("lom_psl", "Regione Lombardia – Pericolosità sismica locale (studi comunali)", A1B, "territorio/pericolosita_sismica_locale", "leaf",
     dict(theme="sismico", legal_ref="D.G.R. Lombardia IX/2616/2011 (componente sismica PGT)", exclude=r"^(Pericolosita|Scenari|AMPLIFIC|INSTAB|CEDIM|COMPORT)")),
    ("lom_ms", "Regione Lombardia – Microzonazione sismica", A1B, "territorio/Microzonazione_sismica", [12, 20],
     dict(theme="sismico", legal_ref="OPCM 4007/2012; studi di microzonazione (livello 1)", info=True)),
    ("lom_fattibilita", "Regione Lombardia – Mosaico della fattibilità geologica", A1B, "territorio/fattibilita_geologica", [88],
     dict(theme="geologico", legal_ref="D.G.R. Lombardia IX/2616/2011 (classi di fattibilità 1-4)", note="Mosaico regionale degli studi comunali; fa fede il PGT vigente.")),
    ("lom_pgt_mosaico", "Regione Lombardia – Mosaico PGT (tavola delle previsioni)", A1B, "territorio/tav_previsioni_b", "leaf",
     dict(theme="urbanistico", legal_ref="L.R. 12/2005 (PGT)", exclude=r"^(Componente geologica|Limiti amministrativi|Comuni poligonali|Province|Fasce di rispetto e limiti|Carta del consumo|Carta consumo|Modalità attuative|Servizi e impianti|Corridoi|Zone riqualificazione|Sportello unico)",
          note="Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.")),
    ("lom_pgt_vincoli", "Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)", A1B, "territorio/mos_tav_b", "leaf",
     dict(theme="urbanistico", legal_ref="L.R. 12/2005; vincoli da PRG/PGT", exclude=r"^(Perimetri dei vincoli|Parchi locali$|Parchi urbani|Vincoli di P\.R\.G\.$|Vincoli derivati da leggi nazionali$|Vincoli derivati da leggi nazionali - Dettaglio)",
          note="Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.")),
    ("lom_azzonamenti", "Regione Lombardia – Azzonamenti comunali", A1B, "territorio/Azzonamenti_comunali", [0],
     dict(theme="urbanistico", legal_ref="Strumento urbanistico comunale", note="Zonizzazione di sintesi: può riferirsi a PRG/PGT non aggiornato; verificare il PGT vigente.")),
    ("lom_stato_pgt", "Regione Lombardia – Stato di avanzamento dei PGT", A1B, "territorio/stato_pgt", [1],
     dict(theme="urbanistico", legal_ref="L.R. 12/2005", info=True)),
    ("lom_foreste", "Regione Lombardia – Foreste (governo, destinazioni, piani di assestamento)", A2, "agricoltura/governo_bosco", [0],
     dict(theme="forestale", legal_ref="L.R. 31/2008; D.Lgs. 34/2018", info=True)),
    ("lom_foreste_dest", "Regione Lombardia – Destinazioni selvicolturali", A2, "agricoltura/destinazioni_selvicolturali", [0],
     dict(theme="forestale", legal_ref="L.R. 31/2008", info=True)),
    ("lom_boschi_protezione", "Regione Lombardia – Boschi di protezione", A2, "sistemiverdi/boschi_protezione", [0],
     dict(theme="forestale", legal_ref="L.R. 31/2008", info=True)),
    ("lom_paf", "Regione Lombardia – Piani di assestamento forestale", A2, "agricoltura/PAF", [0],
     dict(theme="forestale", legal_ref="L.R. 31/2008", info=True)),
    ("lom_beni_culturali", "Regione Lombardia – Beni culturali vincolati (SIRBeC)", A1, "sirbec/BeniCulturaliVincolati", [2, 1, 3],
     dict(theme="culturale", legal_ref=C42 + " Parte II", prox=30, note="Edifici: per il vincolo diretto servono foglio/mappale (Vincoli in Rete).")),
    ("lom_reticolo", "Regione Lombardia – Reticolo idrico (RIP, RIB, RIM)", A1B, "territorio/ReticoloIdrografico_RIRU", [3, 2, 8, 7],
     dict(theme="idraulico", legal_ref="R.D. 523/1904; D.G.R. XII/3668/2024 (reticolo idrico)", prox=15,
          note="Polizia idraulica: le fasce (di norma 10 m) si misurano dal ciglio/piede arginale, non dall'asse.")),
    ("lom_nitrati", "Regione Lombardia – Zone vulnerabili da nitrati", A2, "ambiente/Zone_vulnerabili_nitrati", [1],
     dict(theme="acque", legal_ref="Dir. 91/676/CEE; D.Lgs. 152/2006 art. 92; Reg. reg. nitrati", display_fields=[],
          note="Zona vulnerabile da nitrati di origine agricola (il dato non porta attributi descrittivi utili).")),
    ("lom_siti_contaminati", "Regione Lombardia – Siti contaminati e bonificati", A1.replace("arcgis/", "arcgis4/"), "SISU/SitiContaminatiBonificati", [2, 1, 3],
     dict(theme="suolo e rifiuti", legal_ref="D.Lgs. 152/2006 Parte IV Titolo V", prox=50)),
    ("lom_demanio", "Regione Lombardia – Particelle demaniali", A1B, "territorio/catasto_demanio", [10],
     dict(theme="proprietà", legal_ref="Catasto – demanio", info=True)),
]

BRESCIA_SPEC = [
    ("bs_ptcp_tutele", "Provincia di Brescia – PTCP 2014: tutele paesaggistiche", BS, "ptcp_2014/tav_2_7_Tutele_paesaggistiche", "leaf",
     dict(theme="paesaggistico", legal_ref="PTCP Brescia (DCP 31/2014) – Tav. 2.7", exclude=r"^(Fino a|Da |Confin|Comuni|Province|Limiti)", info=True,
          note="Replica provinciale di dati SIBA/PPR: utile come riscontro incrociato.")),
    ("bs_ptcp_rischi", "Provincia di Brescia – PTCP 2014: ambiente e rischi", BS, "ptcp_2014/tav_3_1_Ambiente_rischi", "leaf",
     dict(theme="idrogeologico", legal_ref="PTCP Brescia – Tav. 3.1", exclude=r"^(Fino a|Da |Confin|Comuni|Province|Limiti)", prox=25)),
    ("bs_ptcp_dissesti", "Provincia di Brescia – PTCP 2014: inventario dei dissesti", BS, "ptcp_2014/tav_3_2_Inventario_dei_dissesti", "leaf",
     dict(theme="idrogeologico", legal_ref="PTCP Brescia – Tav. 3.2", exclude=r"^(Fino a|Da |Confin|Comuni|Province|Limiti)", prox=25)),
    ("bs_ptcp_ambiti_agricoli", "Provincia di Brescia – PTCP 2014: ambiti agricoli strategici", BS, "ptcp_2014/tav_5_Ambiti_agricoli_strategici", "leaf",
     dict(theme="agricolo", legal_ref="PTCP Brescia – Tav. 5; L.R. 12/2005 art. 15", exclude=r"^(Fino a|Da |Confin|Comuni|Province|Limiti|Parchi|Sic|Zps|Laghi|Boschi|Aree sterili|Corridoi)")),
    ("bs_ptcp_rete_ecologica", "Provincia di Brescia – PTCP 2014: rete ecologica", BS, "ptcp_2014/tav_4_Rete_ecologica", "leaf",
     dict(theme="ambientale", legal_ref="PTCP Brescia – Tav. 4", exclude=r"^(Fino a|Da |Confin|Comuni|Province|Limiti)", info=True)),
    ("bs_carta_vincoli", "Provincia di Brescia – Carta dei vincoli (PTCP)", BS, "ambiente/carta_vincoli_2", "leaf",
     dict(theme="ambientale", legal_ref="PTCP Brescia – carta dei vincoli", exclude=r"^(_|#|Confin|Comuni)", info=True)),
    ("bs_pgra", "Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)", BS, "ptcp_adeguamento_ptr/tav_3_4_PGRA", "leaf",
     dict(theme="idraulico", legal_ref="Dir. 2007/60/CE; D.Lgs. 49/2010; PGRA", exclude=r"^(_|#|Confin|Comuni|Province|Limiti|Fino|Da )",
          note="Campo 'aggiorna' = data di aggiornamento del dato.")),
    ("bs_difesa_suolo", "Provincia di Brescia – Difesa del suolo", BS, "urbanistica/difesa_suolo", "leaf",
     dict(theme="idrogeologico", legal_ref="L.R. 12/2005 art. 57; PAI/PGRA", exclude=r"^(_|#|Confin|Comuni|Province|Limiti)", prox=25)),
    ("bs_dlgs42", "Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004", BS, "urbanistica/dlgs42_2004", "leaf",
     dict(theme="paesaggistico", legal_ref=C42 + " artt. 136 e 142", exclude=r"^(_|#|Confin|Comuni|Province|Limiti)")),
    ("bs_vincolo_idrogeologico", "Provincia di Brescia – Vincolo idrogeologico", BS, "vincoli/idro_civ", [0],
     dict(theme="idrogeologico", legal_ref="R.D. 3267/1923; L.R. 31/2008")),
    ("bs_aree_percorse_fuoco", "Provincia di Brescia – Aree percorse dal fuoco", BS, "urbanistica/aree_percorse_97_2021", [0],
     dict(theme="forestale", legal_ref="L. 353/2000 art. 10 (divieti su aree percorse dal fuoco)")),
    ("bs_pif", "Provincia di Brescia – PIF: trasformabilità del bosco", BS, "pif/09_trasformabilita", "leaf",
     dict(theme="forestale", legal_ref="L.R. 31/2008 art. 47 (PIF – trasformabilità)", exclude=r"^(_|#|Confin|Comuni)")),
    ("bs_cave", "Provincia di Brescia – Ambiti territoriali estrattivi (ATE)", BS, "ambiente/ate_cave", "leaf",
     dict(theme="suolo e rifiuti", legal_ref="L.R. 14/1998 (piano cave)", exclude=r"^(_|#|Confin|Comuni)")),
    ("bs_pozzi", "Provincia di Brescia – Pozzi e aree di rispetto", BS, "ambiente/pozzi", "leaf",
     dict(theme="acque", legal_ref="", exclude=r"^(_#Sfondo|Confin|Comuni)", info=True,
          note="Cerchi di 1000 m attorno ai pozzi (livello '_#Raggio del pozzo'): il significato normativo non è documentato nel servizio; non equivale alla zona di rispetto ex art. 94 D.Lgs. 152/2006.")),
    ("bs_rifiuti_vincoli", "Provincia di Brescia – Piano rifiuti: vincoli localizzativi aggregati", BS, "rifiuti/R_12_carta_vincoli_aggregati_per_grado_prescrizione", [3],
     dict(theme="suolo e rifiuti", legal_ref="Piano provinciale rifiuti – criteri localizzativi impianti", note="Vale per la localizzazione di impianti di gestione rifiuti, non come vincolo edilizio generale.", info=True)),
    ("bs_aree_pee", "Provincia di Brescia – Aree di piani di emergenza (dighe)", BS, "protezione_civile/aree_pee", "leaf",
     dict(theme="protezione civile", legal_ref="Piani di emergenza esterna (PEE)", exclude=r"^(_|#|Confin|Comuni)", info=True)),
    ("bs_mosaico_ptcp", "Provincia di Brescia – Mosaico PGT (ATO e destinazioni)", BS, "urbanistica/mosaico_PTCP_2014", [2],
     dict(theme="urbanistico", legal_ref="PTCP Brescia – mosaico dei PGT", info=True)),
]

# Correzioni per difetti noti dei servizi (verificati con query di confronto nativo/WGS84)
LAYER_OVERRIDES = {
    # tav_previsioni_b/31: il server ignora outSR e la riproiezione WGS84->UTM non trova gli elementi; in UTM32N nativo funziona
    ("lom_pgt_mosaico", 31): {"native_sr": 32632},
}

NOISE = re.compile(r"^(OBJECTID.*|FID.*|SHAPE.*|GlobalID|WIZ_.*|.*_FID|CLASSREF|PERIMETER|AREA|LEN|AREA_\d|SHAPE\.?.*|.*ID_?$|.*OBJECTID.*|.*shape_.*|cod_istat.*|COD_PRO.*|SIG_PRO|BELFIORE)$", re.I)
PRIORITY = re.compile(r"(descr|nome|name|tipo|classe|vincolo|denom|legenda|fascia|scenario|scenar|zona|sigla|norma|art|data|anno|aggiorn|stato|fonte|lett|ambito|categ|label)", re.I)
LINKF = re.compile(r"(url|link|immagin|gazzett|scheda|decreti|doc|pdf)", re.I)


def get(url):
    for _ in range(3):
        try:
            return S.get(url, params={"f": "json"}, timeout=60).json()
        except Exception:
            pass
    return {}


def pick_fields(fields):
    cand = [f for f in fields if not NOISE.match(f["name"]) and f["type"] in ("esriFieldTypeString", "esriFieldTypeInteger", "esriFieldTypeSmallInteger", "esriFieldTypeDouble", "esriFieldTypeDate")]
    # i campi Double entrano solo se il nome è significativo (es. ZONA), altrimenti sono misure (aree, lunghezze, quote)
    cand = [f for f in cand if f["type"] != "esriFieldTypeDouble" or PRIORITY.search(f["name"])]
    cand.sort(key=lambda f: (0 if PRIORITY.search(f["name"]) else 1))
    return [f["name"] for f in cand][:6]


def build_source(spec):
    sid, name, base, svc, layers, opt = spec
    url = f"{base}/{svc}/MapServer"
    meta = get(url)
    all_layers = {l["id"]: l for l in meta.get("layers", [])}
    want = [l["id"] for l in meta.get("layers", []) if not l.get("subLayerIds")] if layers == "leaf" else layers
    excl = re.compile(opt["exclude"]) if opt.get("exclude") else None
    out_layers = []

    def one(i):
        d = get(f"{url}/{i}")
        return i, d
    with ThreadPoolExecutor(8) as ex:
        infos = list(ex.map(one, want))
    for i, d in infos:
        if not d or d.get("error") or d.get("subLayers") or d.get("type") not in (None, "Feature Layer"):
            print(f"  [{sid}] salto {i} {all_layers.get(i, {}).get('name')}: gruppo/non interrogabile", file=sys.stderr)
            continue
        if "query" not in (d.get("capabilities") or "Query").lower():
            print(f"  [{sid}] salto {i} {d.get('name')}: senza Query", file=sys.stderr)
            continue
        nm = (d.get("name") or f"livello {i}").strip()
        if excl and excl.search(nm):
            continue
        fields = d.get("fields", [])
        dfields = [f["name"] for f in fields if f["type"] == "esriFieldTypeDate"]
        lay = {"id": i, "name": nm, "geometry": (d.get("geometryType") or "").replace("esriGeometry", "").lower()}
        disp = opt["display_fields"] if "display_fields" in opt else pick_fields(fields)
        lay["display_fields"] = disp
        if [x for x in dfields if x in disp]:
            lay["date_fields"] = [x for x in dfields if x in disp]
        links = [f["name"] for f in fields if f["type"] == "esriFieldTypeString" and LINKF.search(f["name"]) and not NOISE.match(f["name"])]
        if links:
            lay["link_fields"] = links
        if lay["geometry"] in ("polyline", "point", "multipoint"):
            lay["proximity_m"] = opt.get("prox") or 25   # un punto non 'interseca' mai una linea: si cerca entro una distanza
        if opt.get("info"):
            lay["info"] = True
        out_layers.append(lay)
    src = {"id": sid, "name": name, "type": "arcgis", "provider": "Regione Lombardia" if base != BS else "Provincia di Brescia",
           "url": url, "bbox": BRESCIA if base == BS else LOMB, "theme": opt["theme"], "legal_ref": opt.get("legal_ref", ""),
           "value_note": opt.get("note", "Dato ricognitivo: verificare l'atto originario e lo strumento vigente."),
           "applies_if": ({"provincia": ["Brescia"]} if base == BS else {"regione": ["Lombardia"]}), "layers": out_layers}
    if opt.get("info"):
        for l in out_layers:
            l["info"] = True
    for l in out_layers:
        ov = LAYER_OVERRIDES.get((sid, l["id"]))
        if ov:
            l.update(ov)
    return src


def main():
    for fname, spec in (("lombardia.json", LOMBARDIA), ("brescia.json", BRESCIA_SPEC)):
        with ThreadPoolExecutor(4) as ex:
            srcs = list(ex.map(build_source, spec))
        srcs = [s for s in srcs if s["layers"]]
        (OUT / fname).write_text(json.dumps({"sources": srcs}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(fname, len(srcs), "fonti,", sum(len(s["layers"]) for s in srcs), "livelli")


if __name__ == "__main__":
    main()
