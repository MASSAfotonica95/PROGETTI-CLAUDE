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

## Fonti incluse (verificate raggiungibili il 2026-09-30)
Regione Lombardia SIBA (art. 136/142 D.Lgs. 42/2004), EEA Natura 2000 e CDDA, ISPRA mosaicatura PAI frane.
Non raggiungibili dall'ambiente di sviluppo (quindi non integrate): Geoportale Nazionale/PCN, Vincoli in Rete (solo link manuale).
Copertura per altre regioni, PAI idraulico/PGRA, vincolo idrogeologico RDL 3267/1923, PGT comunali: **da aggiungere**.

## Versione web (HTML)
- **`vincoli-web.html`** (27 KB, nessuna installazione): aprilo con doppio clic. Interroga direttamente Regione Lombardia (SIBA), EEA e Nominatim.
- **Modalità completa**: `python -m vincoli.webapp` (o `avvia.bat` / `avvia.sh`), solo libreria standard di Python. Serve la stessa pagina su `http://127.0.0.1:8765/` e aggiunge un proxy locale per le fonti che bloccano le richieste dal browser (oggi **ISPRA**: risponde 403 a ogni richiesta con header `Origin`, e non invia CORS). Il proxy accetta solo HTTPS verso host elencati nel registro (`"browser_proxy": true`), non segue redirect e rifiuta Host/Origin non locali.
- Senza proxy le fonti non raggiungibili risultano **NON VERIFICATO** con la spiegazione, mai "nessun vincolo".
- Rigenerare l'HTML dopo aver modificato il registro: `python -m vincoli.webapp --export vincoli-web.html`.
- `.exe` (non costruito né testato qui): `pip install pyinstaller && pyinstaller --onefile --add-data "vincoli/web;vincoli/web" --add-data "vincoli/sources;vincoli/sources" -n vincoli-web vincoli/webapp.py` (su Linux/macOS il separatore di `--add-data` è `:`).
- Il registro delle fonti è lo stesso del CLI; la versione web supporta i tipi `arcgis`, `wfs`, `manual` (non `wms`).
