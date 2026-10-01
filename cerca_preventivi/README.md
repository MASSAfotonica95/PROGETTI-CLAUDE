# cerca_preventivi

Cerca in intere cartelle (e sottocartelle) i **preventivi emessi dal Per. Agr. Angelo
Chiminelli**. Scarta i preventivi di altre ditte e professionisti, anche quando citano
Chiminelli come destinatario, committente o direttore dei lavori.

Il principio guida è questo:
> la parola "preventivo/offerta" individua un *candidato*; è **l'identità dell'emittente**
> a decidere se il documento è davvero di Chiminelli.

L'archivio originale **non viene mai modificato**: il sistema produce un report e, se richiesto,
delle copie.

## Pipeline

```
cartelle ─► 1. scansione ricorsiva  (.pdf .doc .docx .rtf + .p7m firmati; ignora ~$*, nascosti)
         ─► 2. filtro nome file     (preventiv, offert, quotazion, computo, parcell, prev, ...)
                                     disattivabile con --tutti
         ─► 3. apertura/estrazione  .p7m  → busta CAdES aperta in Python puro (DER/BER, base64/PEM,
                                            buste annidate) + nome del FIRMATARIO dal certificato
                                     .docx → testo + intestazioni/piè di pagina + autore (metadati)
                                     .pdf  → pdftotext o pypdf; OCR (tesseract) se scansione e --ocr
                                     .doc  → antiword / catdoc / LibreOffice; altrimenti ripiego interno
                                     il formato reale si riconosce dai primi byte, non dall'estensione
         ─► 4. due punteggi         "è un preventivo?"  +  "l'emittente è Chiminelli?"
         ─► 5. esito + prove        report CSV (Excel) + JSON, copie opzionali per esito
```

### Esiti

| Esito | Significato |
|---|---|
| `CONFERMATO` | preventivo, punteggio emittente ≥ 9 |
| `PROBABILE` | preventivo, punteggio emittente 5–8 |
| `DA_VERIFICARE` | indizi contrastanti, testo assente (scansione) o nome file "preventivo" con contenuto atipico |
| `SCARTATO` | preventivo di un altro emittente (punteggio ≤ 0) |
| `NON_PREVENTIVO` | il contenuto non è un preventivo |
| `ERRORE` | file illeggibile (p7m rovinato, firma *detached*, ecc.) |

Le soglie sono modificabili nel file di configurazione.

### Come viene riconosciuto l'emittente (punteggio)

| Indizio | Punti |
|---|---:|
| `.p7m` firmato digitalmente da Chiminelli / da un altro soggetto | +8 / −4 |
| nome nell'intestazione o nel piè di pagina del `.docx` (+2 se c'è "Per. Agr.") | +5 |
| nome completo in intestazione o in firma ("In fede", "Il tecnico", ...) | +5 |
| solo cognome nella stessa posizione | +3 |
| "Per. Agr." / "Perito agrario" accanto al nome | +3 |
| preceduto da "Il tecnico", "In fede", "Studio tecnico", ... | +2 |
| nome citato solo nel corpo del testo | +1 |
| P.IVA, CF, email, PEC, telefono, n. iscrizione (da config) | +4 ciascuno (max +8) |
| dicitura esatta della carta intestata (config) | +4 (max +8) |
| righe dell'**impronta** appresa dai preventivi certi | +2 (max +6) |
| autore nei metadati del file | +2 |
| voci di onorario/prestazione professionale / voci da ditta (posa in opera, manodopera, ...) | +1 / −1 |
| **nome presente solo come destinatario/committente/D.L.** ("Spett.le", "Alla c.a.", "Committente:", "Direzione lavori:", ...) | −3 |
| intestazione di società/ditta (S.r.l., S.n.c., Impresa, Ditta, ...) che non sia il destinatario | −3 |
| intestazione di un altro professionista (Geom., Ing., Arch., **Dott. Agr.**, ...) | −2 |
| P.IVA di altri soggetti (se è configurata quella di Chiminelli e non compare) | −2 |
| emittente presente nella lista `emittenti_esclusi` | −6 |
| il nome non compare affatto | −3 |

Per decidere tra destinatario e autore si guarda il **marcatore più vicino che precede il nome**,
entro 150 caratteri. Gli identificativi e le righe dell'impronta che si trovano nel blocco del
destinatario (per esempio l'indirizzo o l'email di Chiminelli nell'offerta di una ditta) **non
vengono contati**. Il riconoscimento del cognome tollera i tipici errori dell'OCR
(`Chlmine1li`) e le lettere spaziate (`C H I M I N E L L I`).

Per ogni file il report riporta: **motivazioni con i punti**, un **estratto di testo con il
numero di pagina**, emittente presunto, oggetto, importo, data, tipo di prestazione (indicativo,
ricavato dalle parole chiave), firmatari del `.p7m`, autore nei metadati e hash SHA-256. Se lo
stesso documento compare più volte (anche come `x.pdf` e `x.pdf.p7m`), viene segnalato come
duplicato.

## Uso

```bash
# 1) configurazione: copiare config.esempio.json in config.json e compilare gli identificativi
# 2) (consigliato) imparare l'impronta da 3-10 preventivi SICURAMENTE di Chiminelli
python cerca_preventivi.py --impara "D:\Esempi_certi" -c config.json
# 3) scansione
python cerca_preventivi.py "D:\Archivio" -c config.json -o report.csv
python cerca_preventivi.py "D:\Archivio" -c config.json --tutti --ocr --cache indice.sqlite --copia D:\Risultati
```

| Opzione | Effetto |
|---|---|
| `--tutti` | analizza il contenuto di tutti i file, non solo quelli con il nome da preventivo |
| `--ocr` | esegue l'OCR delle prime 2 pagine dei PDF senza testo (servono `tesseract` con lingua `ita` e `pdftoppm`) |
| `--cache indice.sqlite` | scansione incrementale: i file non modificati non vengono riletti (si conserva il testo, quindi se si cambia la configurazione la riclassificazione è immediata) |
| `--copia DIR` | copia CONFERMATI e PROBABILI in `DIR/01_CONFERMATO/...` e `DIR/02_PROBABILE/...`, mantenendo le sottocartelle (`--copia-anche-dubbi` per includere DA_VERIFICARE) |
| `--impara ESEMPI` | salva in `config.json` le righe di intestazione/firma che ricorrono in almeno metà degli esempi. **Controllare l'elenco stampato** |
| `-v` | stampa l'esito di ogni file |

**Interfaccia grafica**: `python gui.py` (su Windows doppio clic su `avvia_gui.bat`). Permette di
scegliere la cartella, avviare la scansione, vedere i risultati, mostrare l'evidenza, aprire il
documento o la cartella e aprire il report in Excel.

## Installazione

Serve Python 3.9 o superiore. Il codice usa solo la libreria standard; consigliati:

```bash
pip install -r requirements.txt     # pypdf, cryptography
```

Strumenti esterni facoltativi, usati se presenti nel PATH: `pdftotext`/`pdfinfo` (poppler),
`antiword` o `catdoc` oppure LibreOffice (`soffice`) per i `.doc`, `tesseract` + `pdftoppm` per l'OCR.
Senza nessun programma per i `.doc` si usa un ripiego interno che estrae le stringhe dal file
binario: è meno preciso e il report lo segnala.

## Test

```bash
cd cerca_preventivi
python -m unittest discover -s tests
python tests/campioni.py archivio_di_prova    # genera un archivio fittizio da provare
```

L'archivio di prova contiene, con dati fittizi: preventivi di Chiminelli in `.docx`, `.pdf` e
`.pdf.p7m` firmato; l'offerta di una ditta elettrica *indirizzata* a Chiminelli; il preventivo di
un'impresa con Chiminelli *direttore dei lavori*; il preventivo di un geometra; l'offerta firmata
di un vivaio; una fattura `.xml.p7m` (da ignorare); un duplicato; un file con nome non indicativo.

## Limiti noti

- I punteggi sono stati tarati su documenti **fittizi**: prima dell'uso vanno verificati sui
  preventivi reali, controllando i `DA_VERIFICARE` e un campione di `SCARTATI`.
- Se la carta intestata è un'**immagine** (logo con il nome), il nome non viene letto, a meno che
  non compaia anche in firma, nei metadati o nel certificato `.p7m`. Gli identificativi in
  `config.json` e l'impronta compensano in parte.
- I `.p7m` con firma *detached* (il documento non è dentro la busta) risultano `ERRORE`.
- Oggetto, importo e tipo di prestazione sono estratti con espressioni regolari: hanno valore
  indicativo.

## Possibili sviluppi

- Mandare i soli `DA_VERIFICARE` a un modello linguistico, anche locale, con una richiesta del tipo
  "chi emette il documento, a chi è rivolto? rispondi in JSON".
- Esportazione `.xlsx` con filtri, tramite `openpyxl`.
