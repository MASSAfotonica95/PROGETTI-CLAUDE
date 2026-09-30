# Vincoli territoriali su coordinata

Dato un punto (WGS84 o UTM ETRS89), interroga in parallelo servizi web pubblici (ArcGIS REST, WFS, WMS)
e produce un report per tema: **INTERCETTATO / ENTRO_RAGGIO / NESSUN_ELEMENTO / NON_VERIFICATO / VERIFICA_MANUALE**,
con fonte, norma, atto collegato e URL della query riproducibile.

```bash
pip install requests
python -m vincoli "45.54667794588481,10.227873542813938" --radius 300        # report Markdown
python -m vincoli --utm 595850.405 5044415.501 32 --format json
python -m vincoli --list-sources
python -m unittest discover -s tests -t .
```

## Regole di affidabilità
- `NESSUN_ELEMENTO` solo se il servizio ha risposto correttamente con zero elementi; errori, timeout o blocchi → `NON_VERIFICATO`, mai "nessun vincolo".
- Ogni esito cita fonte, livello, data/ora e query. L'esito è **ricognitivo, non certificativo** (il valore probatorio spetta al CDU, art. 30 DPR 380/2001, e agli atti originari).
- Le fonti senza API (PGT comunali, Vincoli in Rete, CDU) sono `VERIFICA_MANUALE`: il sistema non ne inventa l'esito.
- WFS: il filtro usa `SRID=4326;POINT(lon lat)`; senza SRID GeoServer legge le coordinate nel CRS nativo e restituisce risultati vuoti.
- WMS GetFeatureInfo ha tolleranza in pixel: risultato approssimato (segnalato nel report).

## Aggiungere fonti (senza toccare il codice)
Crea un `.json` in `vincoli/sources/` o in una cartella passata con `--sources-dir`, stesso schema di
`vincoli/sources/italia.json`: `type` (`arcgis`|`wfs`|`wms`|`manual`), `url`, `bbox` [lonmin,latmin,lonmax,latmax],
`layers`, opzionale `applies_if: {"comune": [...]}`. Servizi privati con credenziali: estendere `http.make_session` (header/token).

## Fonti incluse (Lombardia e provincia di Brescia: 373 livelli, verificati)
- **Regione Lombardia** (server ArcGIS del Geoportale): vincoli paesaggistici SIBA (artt. 136/142), Piano Paesaggistico Regionale (con siti UNESCO), aree protette/PLIS/Natura 2000/RER, PAI vigente, IFFI, PGRA, vincolo idrogeologico, classificazione sismica, pericolosità sismica locale, microzonazione, fattibilità geologica, **Mosaico PGT** (nuclei di antica formazione, sensibilità paesistica, fasce di rispetto stradali/ferroviarie/cimiteriali/pozzi/depuratori, servitù militari, limitazioni aeroportuali), azzonamenti, reticolo idrico, beni culturali vincolati, siti contaminati, nitrati.
- **Provincia di Brescia** (SIT provinciale): PTCP 2014 (tutele, ambiente e rischi, dissesti, ambiti agricoli strategici), PGRA aggiornato 2025, difesa del suolo, D.Lgs. 42/2004, vincolo idrogeologico, aree percorse dal fuoco, PIF (trasformabilità boschi), cave.
- **EEA** (Natura 2000, CDDA) e **ISPRA** (mosaicatura PAI frane) su tutto il territorio.
- Le fonti senza API (PGT del Comune, CDU, Vincoli in Rete) restano `VERIFICA_MANUALE`.
- Non trovati servizi interrogabili del Comune di Brescia (PGT vigente) né ENAC; il Geoportale Nazionale/Vincoli in Rete non sono raggiungibili da script.

## Qualità dei dati: autotest e rigenerazione
- `python -m vincoli --selftest` – per ogni livello prende un elemento reale e verifica che il servizio lo restituisca sul suo stesso punto (controllo positivo). Senza, un «nessun elemento» non prova nulla. Ultimo esito: 372/372 livelli OK (durata ~5 min).
- `python tools/build_registry.py` – rigenera `vincoli/sources/lombardia.json` e `brescia.json` dai metadati live dei servizi (scarta i gruppi, sceglie i campi, riconosce date e link). Il giudizio umano (tema, norma, livelli «informativi», difetti noti in `LAYER_OVERRIDES`) sta in `tools/build_registry.py`.
- I livelli «informativi» (contesto, non vincoli) si interrogano con `--all` (web: casella «livelli informativi»).
- Livelli lineari/puntuali: si cerca entro una distanza fissa (`proximity_m`) e l'esito è `ENTRO_RAGGIO`, mai «sul punto».
- Riproiezione: il server converte WGS84→UTM32N; confronto nativo/WGS84 su particelle di 70–5000 m² → nessuna differenza (celle da 2 m). Un livello difettoso (Mosaico PGT, fasce pozzi) si interroga in UTM nativo.
- Tutti i dati sono **ricognitivi**: per valore probatorio CDU (art. 30 DPR 380/2001) e atti originari.
