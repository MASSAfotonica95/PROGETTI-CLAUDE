# Esempio documentato – via Giovanni Lipella, Brescia

Report generato il 2026-09-30 con `python -m vincoli "45.54667794588481,10.227873542813938" --radius 300 --all`
(373 livelli interrogati, nessun errore di servizio). Il testo completo segue dopo questo riepilogo.

## Riepilogo dei fatti emersi dai servizi (sul punto)
| Tema | Esito | Fonte (livello) |
|---|---|---|
| Vincolo paesaggistico art. 136 D.Lgs. 42/2004 | **Sul punto**: D.M. 24/05/1952 "Zona circostante il castello, Brescia" (comunicazione 15/06/1950) | SIBA Lombardia (3 livelli), PTCP Brescia Tav. 2.7, Provincia D.Lgs. 42/2004 |
| Zona sismica del comune | **Zona 2** | Regione Lombardia – classificazione sismica (campo ZONA=2) |
| Pericolosità sismica locale | **Z4b** (amplificazioni litologiche e geometriche) | studi comunali (Regione) e Mosaico PGT |
| Fattibilità geologica | **Classe 2** (modeste limitazioni) | Mosaico regionale, Mosaico PGT, Attestato del territorio |
| Sensibilità paesistica (PGT) | **Classe 4 – elevata** | Mosaico PGT (scheda PDF collegata) |
| Zonizzazione | TUC residenziale (Mosaico PGT); zona "B3R2" art. 73 del PRG (Azzonamenti, dato storico) | Regione Lombardia |
| Stato del PGT | fase "Approvazione" | Regione Lombardia – stato PGT |
| Classificazione acustica | Classe 3 | Attestato del territorio |
| Zona vulnerabile da nitrati | Sì | Regione Lombardia |

## Entro 300 m (non sul punto)
PLIS "Parco delle Colline di Brescia" · buffer zone UNESCO "I Longobardi in Italia" (COD 1318) · D.M. 20/03/1958 (Ronchi) e D.M. 30/10/1961 (Costalunga) ·
bosco (art. 142 lett. g) · aree di frana quiescente e pericolosità da frana "Elevata P3" (ISPRA) · fattibilità classi 3 e 4 · reticolo idrico minore e di bonifica.

## Non emerso dai servizi
Il D.M. 08/10/1955 "Oriente la Pusterla" e il D.M. "18 giugno 1952" non compaiono sul punto né entro 300 m nei livelli SIBA interrogati.
Vincolo idrogeologico (R.D. 3267/1923), fasce PAI/PGRA, SIC/ZPS, parchi regionali: nessun elemento sul punto.
Restano **da verificare sulle fonti originarie**: vincoli diretti su edifici (servono foglio/mappale), tavole PGT vigenti del Comune (V-PR06/11/12), limitazioni ENAC, CDU.

---

# Verifica vincoli – 45.546678, 10.227874

- WGS84 (EPSG:4326): 45.546677946, 10.227873543
- ETRS89/UTM 32N (EPSG:25832): E 595850.405 N 5044415.502 · UTM 33N (EPSG:25833): E 127485.200 N 5054768.767
- Località (da OpenStreetMap Nominatim (ODbL), indicativa): Via Giovanni Lipella, Brescia (Brescia), Lombardia
- Raggio di ricerca aggiuntivo: 300 m
- Livelli interrogati: 373

**Riepilogo:** 🔴 INTERCETTATO: 36 · 🟠 ENTRO_RAGGIO: 56 · 📄 VERIFICA_MANUALE: 6 · 🟢 NESSUN_ELEMENTO: 336

> Esito ricognitivo a scopo conoscitivo: NON ha valore certificativo. "Nessun elemento" vale solo per il livello interrogato e solo se il servizio ha risposto. Per valore probatorio: Certificato di Destinazione Urbanistica (art. 30 DPR 380/2001) e atti originari.

## Vincoli intercettati sul punto
#### Tema: acque
### 🔴 Grado di vulnerabilità intrinseca degli acquiferi lombardi
- Stato: **INTERCETTATO** · Tema: acque · Norma: D.Lgs. 152/2006 (tutela acque sotterranee)
- Fonte: Regione Lombardia – Vulnerabilità intrinseca degli acquiferi (Regione Lombardia)
  - VULN_INTEG=BASSO
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/63/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Zone vulnerabili da nitrati di origine agricola
- Stato: **INTERCETTATO** · Tema: acque · Norma: Dir. 91/676/CEE; D.Lgs. 152/2006 art. 92; Reg. reg. nitrati
- Fonte: Regione Lombardia – Zone vulnerabili da nitrati (Regione Lombardia)
  - (nessun attributo descrittivo)
- Valore del dato: Zona vulnerabile da nitrati di origine agricola (il dato non porta attributi descrittivi utili).
- Query (riproducibile, 2026-09-30T22:42:30+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/ambiente/Zone_vulnerabili_nitrati/MapServer/1/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 _#Raggio del pozzo
- Stato: **INTERCETTATO** · Tema: acque
- Fonte: Provincia di Brescia – Pozzi e aree di rispetto (Provincia di Brescia)
  - cod_pozzo=170290133
  - cod_pozzo=170290151
  - cod_pozzo=170290154
  - cod_pozzo=170290322
  - cod_pozzo=170290406
- Valore del dato: Cerchi di 1000 m attorno ai pozzi (livello '_#Raggio del pozzo'): il significato normativo non è documentato nel servizio; non equivale alla zona di rispetto ex art. 94 D.Lgs. 152/2006.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ambiente/pozzi/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: ambientale
### 🔴 Ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Stato: **INTERCETTATO** · Tema: ambientale · Norma: PTCP Brescia – Tav. 4
- Fonte: Provincia di Brescia – PTCP 2014: rete ecologica (Provincia di Brescia)
  - descri=ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa; normativa=art.51 - ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:15+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_4_Rete_ecologica/MapServer/15/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Stato: **INTERCETTATO** · Tema: ambientale · Norma: PTCP Brescia – carta dei vincoli
- Fonte: Provincia di Brescia – Carta dei vincoli (PTCP) (Provincia di Brescia)
  - descri=ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa; normativa=art.51 - ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:16+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ambiente/carta_vincoli_2/MapServer/22/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: contesto
### 🔴 Classificazione acustica comunale - piani acustici
- Stato: **INTERCETTATO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - CLASSE_ACU=3
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 DUSAF - Uso del suolo
- Stato: **INTERCETTATO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - descrizione=Tessuto residenziale denso
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/57/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Piano Emergenza Comunale
- Stato: **INTERCETTATO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - PEC=presente
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/71/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Zona omogenea allerta idro-meteo
- Stato: **INTERCETTATO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - NOME_IM=Alta pianura orientale; CODICE_IM=IM-11
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/67/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Zona omogenea allerta incendi boschivi
- Stato: **INTERCETTATO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - NOME_AREA=Mella - Chiesa; COD_AREA=F10
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/70/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Zona omogenea allerta neve
- Stato: **INTERCETTATO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - Cod_Zona=NV-14; Descr_Zona=Alta pianura bresciana
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/68/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: geologico
### 🔴 Mosaico della fattibilità
- Stato: **INTERCETTATO** · Tema: geologico · Norma: D.G.R. Lombardia IX/2616/2011 (classi di fattibilità 1-4)
- Fonte: Regione Lombardia – Mosaico della fattibilità geologica (Regione Lombardia)
  - CLASSE_FATTIBILITA=CLASSE 2; INFO_CLASSE_FATTIB=FATTIBILITA' CON MODESTE LIMITAZIONI; ISTAT_COMUNE=017029; COMUNE=Brescia; BASE_RILIEVO=FOTOGRAMMETRICO; SCALA_RILIEVO=1:5000
- Valore del dato: Mosaico regionale degli studi comunali; fa fede il PGT vigente.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/fattibilita_geologica/MapServer/88/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: idrogeologico
### 🔴 Area di ricarica potenziale: Gruppo A
- Stato: **INTERCETTATO** · Tema: idrogeologico · Norma: PTCP Brescia – Tav. 3.1
- Fonte: Provincia di Brescia – PTCP 2014: ambiente e rischi (Provincia di Brescia)
  - descri=Gruppo A; cap=M: moderata
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:13+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_3_1_Ambiente_rischi/MapServer/8/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Area di ricarica potenziale: Gruppo B
- Stato: **INTERCETTATO** · Tema: idrogeologico · Norma: PTCP Brescia – Tav. 3.1
- Fonte: Provincia di Brescia – PTCP 2014: ambiente e rischi (Provincia di Brescia)
  - descri=Gruppo B; cap=M: moderata
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:13+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_3_1_Ambiente_rischi/MapServer/9/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: paesaggistico
### 🔴 Aree di notevole interesse pubblico
- Stato: **INTERCETTATO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Regione Lombardia – Vincoli paesaggistici (SIBA) (Regione Lombardia)
  - DATA_DEC=24/05/1952; DATA_COM=15/06/1950; DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; DORIG_DEC=Decreto Ministeriale; COD_DEC=14
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d14_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_14_Brescia.pdf
- Valore del dato: Ricognitivo: verificare decreto/GU e cartografia originale.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/vincoli_paesaggistici/MapServer/14/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Bellezze d'insieme (D.Lgs. 42/2004 art. 136, comma 1, lettere c e d, e art. 157; ex L. 1497/39)
- Stato: **INTERCETTATO** · Tema: paesaggistico · Norma: PTCP Brescia (DCP 31/2014) – Tav. 2.7
- Fonte: Provincia di Brescia – PTCP 2014: tutele paesaggistiche (Provincia di Brescia)
  - immagini=https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d14_1.pdf; desc_decr2=Zona circostante il castello,  Brescia; conta=79; zz=mapsiba20/verbali_ba_siba/d14_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d14_1.pdf
- Valore del dato: Replica provinciale di dati SIBA/PPR: utile come riscontro incrociato.
- Query (riproducibile, 2026-09-30T22:42:12+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_2_7_Tutele_paesaggistiche/MapServer/19/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Fasce di paesaggio
- Stato: **INTERCETTATO** · Tema: paesaggistico · Norma: PPR Lombardia
- Fonte: Regione Lombardia – Paesaggio: unità tipologiche (Regione Lombardia)
  - FASCIA=FASCIA DELLA BASSA PIANURA; UNIT_PAES=PAESAGGI DELLA PIANURA CEREALICOLA
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:23+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/paesaggio_indirizzi/MapServer/7/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Perimetro delle Aree di notevole interesse pubblico
- Stato: **INTERCETTATO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Regione Lombardia – Vincoli paesaggistici (SIBA) (Regione Lombardia)
  - DATA_DEC=24/05/1952; DATA_COM=15/06/1950; DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; DORIG_DEC=Decreto Ministeriale; COD_DEC=14
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d14_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_14_Brescia.pdf
- Valore del dato: Ricognitivo: verificare decreto/GU e cartografia originale.
- Query (riproducibile, 2026-09-30T22:42:20+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/vincoli_paesaggistici/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Perimetro e Aree di notevole interesse pubblico (D.Lgs. 42/2004 art. 136, comma 1, lettere c e d, e art. 157)
- Stato: **INTERCETTATO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004 (Provincia di Brescia)
  - DATA_DEC=24/05/1952; DATA_COM=15/06/1950; FONTE_BA=120; DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; TIPO_CA=204; DTIPO_CA=Altra cartografia di tipo non valutabile
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/verbali_ba_siba/d14_1.pdf
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/gu_ba_siba/GU_14_Brescia.pdf
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:18+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/dlgs42_2004/MapServer/4/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Unità tipologiche di paesaggio
- Stato: **INTERCETTATO** · Tema: paesaggistico · Norma: PPR Lombardia
- Fonte: Regione Lombardia – Paesaggio: unità tipologiche (Regione Lombardia)
  - FASCIA=FASCIA DELLA BASSA PIANURA; UNIT_PAES=PAESAGGI DELLA PIANURA CEREALICOLA
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:23+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/paesaggio_indirizzi/MapServer/8/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: protezione civile
### 🔴 Limiti comunali
- Stato: **INTERCETTATO** · Tema: protezione civile · Norma: Piani di emergenza esterna (PEE)
- Fonte: Provincia di Brescia – Aree di piani di emergenza (dighe) (Provincia di Brescia)
  - comune=BRESCIA
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/protezione_civile/aree_pee/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: sismico
### 🔴 Aree stabili e aree stabili suscettibili di amplificazioni locali
- Stato: **INTERCETTATO** · Tema: sismico · Norma: OPCM 4007/2012; studi di microzonazione (livello 1)
- Fonte: Regione Lombardia – Microzonazione sismica (Regione Lombardia)
  - Tipo_z=2008; ID_z=33; URL=https://www.cartografia.servizirl.it/download/sismica/2008_017029.jpg; Comune=Brescia
  - Documento: https://www.cartografia.servizirl.it/download/sismica/2008_017029.jpg
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/Microzonazione_sismica/MapServer/20/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Terreni di copertura e substrato geologico
- Stato: **INTERCETTATO** · Tema: sismico · Norma: OPCM 4007/2012; studi di microzonazione (livello 1)
- Fonte: Regione Lombardia – Microzonazione sismica (Regione Lombardia)
  - Tipo_gt=CL; Stato=24; DESCR=Argille inorganiche di medio-bassa plasticita', argille ghiaiose o sabbiose, argille limose, argille magre; ID_gt=40; Gen=ec; Comune=Brescia
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/Microzonazione_sismica/MapServer/12/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Z4b - Zona pedemontana di falda di detrito, conoide alluvionale e conoide deltizio-lacustre
- Stato: **INTERCETTATO** · Tema: sismico · Norma: D.G.R. Lombardia IX/2616/2011 (componente sismica PGT)
- Fonte: Regione Lombardia – Pericolosità sismica locale (studi comunali) (Regione Lombardia)
  - SIGLA=Z4b; DESCRIZIONE=Zona pedemontana di falda di detrito, conoide alluvionale e conoide deltizio-lacustre; EFFETTI=AMPLIFICAZIONI LITOLOGICHE E GEOMETRICHE
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:26+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/pericolosita_sismica_locale/MapServer/106/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Zone sismiche
- Stato: **INTERCETTATO** · Tema: sismico · Norma: OPCM 3274/2003; D.G.R. Lombardia X/2129/2014
- Fonte: Regione Lombardia – Classificazione sismica dei comuni (Regione Lombardia)
  - NOME_COM=BRESCIA; NOME_PRO=BRESCIA; ZONA=2
- Valore del dato: Classificazione vigente: fa fede l'ultimo atto regionale.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/protciv/classificazione_sismica/MapServer/0/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: suolo e rifiuti
### 🔴 Vincoli aggregati
- Stato: **INTERCETTATO** · Tema: suolo e rifiuti · Norma: Piano provinciale rifiuti – criteri localizzativi impianti
- Fonte: Provincia di Brescia – Piano rifiuti: vincoli localizzativi aggregati (Provincia di Brescia)
  - tipo=Aree interessate da vincoli escludenti
- Valore del dato: Vale per la localizzazione di impianti di gestione rifiuti, non come vincolo edilizio generale.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/rifiuti/R_12_carta_vincoli_aggregati_per_grado_prescrizione/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
#### Tema: urbanistico
### 🔴 Ambiti del tessuto urbano consolidato
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=696; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_08.pdf
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:28+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/20/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Aree critiche rete ecologica comunale
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - DESCR_CRITICITA=Residenziale; NOME_COMUNE=BRESCIA; DATA_INIZIO=2022-03-16; COD_CRITICITA=19; NOTE=02_Perimetro_Tessuto_Urbano_Consolidato
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/6/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Azzonamenti comunali
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: Strumento urbanistico comunale
- Fonte: Regione Lombardia – Azzonamenti comunali (Regione Lombardia)
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=CART; DESCRI_PRG=VINCOLO EX LEGE 490/99 ART. 139 - LETTERE C E D; COMUNE=BRESCIA; PRG=V490/99/CD
- Valore del dato: Zonizzazione di sintesi: può riferirsi a PRG/PGT non aggiornato; verificare il PGT vigente.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/Azzonamenti_comunali/MapServer/0/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Classi di sensibilità paesistica
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3730; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:28+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/22/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Fattibilità geologica
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME=Brescia; DESCR_FATTIBILITA=Fattibilità con modeste limitazioni; NOME_COMUNE=BRESCIA
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Pericolosità sismica poligonale
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME=Brescia; TIPOLOGIA=Z4b; DESCR_TIPOLOGIA=Zona pedemontana di falda di detrito, conoide alluvionale e conoide deltizio-lacustre; NOME_COMUNE=BRESCIA; DATA_INIZIO=2019-06-12
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Stato
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005
- Fonte: Regione Lombardia – Stato di avanzamento dei PGT (Regione Lombardia)
  - NOME_COM=BRESCIA; FASE=Approvazione
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/stato_pgt/MapServer/1/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Vincoli di P.R.G. - Aree di rispetto
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - (nessun attributo descrittivo)
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/12/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 Vincoli paesaggistici
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - NOME_CO=BRESCIA; NOME_COD_VINC=Vincolo paesaggistico (L. 1497/39); NOME_VINC_PRINC=Vincolo paesaggistico (L. 1497/39; COD_VINC=50
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/18/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>
### 🔴 mosaico PTCP 2014
- Stato: **INTERCETTATO** · Tema: urbanistico · Norma: PTCP Brescia – mosaico dei PGT
- Fonte: Provincia di Brescia – Mosaico PGT (ATO e destinazioni) (Provincia di Brescia)
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/mosaico_PTCP_2014/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json>

## Elementi entro il raggio
#### Tema: acque
### 🟠 _#Raggio del pozzo
- Stato: **ENTRO_RAGGIO** · Tema: acque
- Fonte: Provincia di Brescia – Pozzi e aree di rispetto (Provincia di Brescia)
  - cod_pozzo=170290043
  - cod_pozzo=170290046
  - cod_pozzo=170290047
  - cod_pozzo=170290108
  - cod_pozzo=170290190
  - cod_pozzo=170290393
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Cerchi di 1000 m attorno ai pozzi (livello '_#Raggio del pozzo'): il significato normativo non è documentato nel servizio; non equivale alla zona di rispetto ex art. 94 D.Lgs. 152/2006.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ambiente/pozzi/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: ambientale
### 🟠 Ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Stato: **ENTRO_RAGGIO** · Tema: ambientale · Norma: PTCP Brescia – Tav. 4
- Fonte: Provincia di Brescia – PTCP 2014: rete ecologica (Provincia di Brescia)
  - descri=ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa; normativa=art.51 - ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:15+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_4_Rete_ecologica/MapServer/15/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Stato: **ENTRO_RAGGIO** · Tema: ambientale · Norma: PTCP Brescia – carta dei vincoli
- Fonte: Provincia di Brescia – Carta dei vincoli (PTCP) (Provincia di Brescia)
  - descri=ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa; normativa=art.51 - ambiti urbani e periurbani preferenziali per la ricostruzione ecologica diffusa
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:16+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ambiente/carta_vincoli_2/MapServer/22/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 ELEMENTI DI SECONDO LIVELLO DELLA RER
- Stato: **ENTRO_RAGGIO** · Tema: ambientale · Norma: DGR 8/10962/2009 (RER)
- Fonte: Regione Lombardia – Rete Ecologica Regionale (Regione Lombardia)
  - (nessun attributo descrittivo)
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:23+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/rete_ecologica_regionale/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Parchi locali di interesse sovracomunale
- Stato: **ENTRO_RAGGIO** · Tema: ambientale · Norma: L. 394/1991; L.R. 86/1983; PLIS: L.R. 86/1983 art. 34
- Fonte: Regione Lombardia – Aree protette (Regione Lombardia)
  - DATA_RIC=1996-05-31; DATA_ULTIM=2024-10-08; DTIPO_PLIS=PLIS provinciale; NOME_PLIS=Parco delle Colline di Brescia; ATTO_RIC=D.g.r. n. 13877; ENTE_PLIS=Convenzione per la gestione associata tra i Comuni di Bovezzo, Brescia, Collebeato, Cellatica, Rodengo Saiano
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato regionale; verificare l'atto istitutivo.
- Query (riproducibile, 2026-09-30T22:42:23+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/ambiente/AreeProtette/MapServer/11/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Rete della viabilità locale
- Stato: **ENTRO_RAGGIO** · Tema: ambientale · Norma: PTCP Brescia – carta dei vincoli
- Fonte: Provincia di Brescia – Carta dei vincoli (PTCP) (Provincia di Brescia)
  - istat=17029; com=BRESCIA; strad_inte=Strada Comunale
  - istat=17029; com=BRESCIA; strad_inte=Strada Comunale
  - istat=17029; com=BRESCIA; strad_inte=Strada Comunale
  - istat=17029; com=BRESCIA; strad_inte=Strada Comunale
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:15+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ambiente/carta_vincoli_2/MapServer/7/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: contesto
### 🟠 Classificazione acustica comunale - piani acustici
- Stato: **ENTRO_RAGGIO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - CLASSE_ACU=4
  - CLASSE_ACU=2
  - CLASSE_ACU=2
  - CLASSE_ACU=3
  - CLASSE_ACU=3
  - CLASSE_ACU=1
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 DUSAF - Uso del suolo
- Stato: **ENTRO_RAGGIO** · Tema: contesto
- Fonte: Regione Lombardia – Attestato del territorio (contesto) (Regione Lombardia)
  - descrizione=Tessuto residenziale continuo mediamente denso
  - descrizione=Tessuto residenziale discontinuo
  - descrizione=Tessuto residenziale rado e nucleiforme
  - descrizione=Insediamenti industriali, artigianali, commerciali
  - descrizione=Parchi e giardini
  - descrizione=Seminativi semplici
  - descrizione=Vigneti
  - descrizione=Prati permanenti con presenza di specie arboree ed arbustive sparse
  - descrizione=Boschi di latifoglie a densità media e alta governati a ceduo
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/protciv/attestato_territorio_master/MapServer/57/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: culturale
### 🟠 Edificio segnalato TCI
- Stato: **ENTRO_RAGGIO** · Tema: culturale · Norma: D.Lgs. 42/2004 Parte II
- Fonte: Regione Lombardia – Beni culturali vincolati (SIRBeC) (Regione Lombardia)
  - NOME=ARCHIVIO DI STATO; PROVINCIA=BS; COMUNE=Brescia; VINCOLATO=NO; TCI=SI
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Edifici: per il vincolo diretto servono foglio/mappale (Vincoli in Rete).
- Query (riproducibile, 2026-09-30T22:42:30+00:00): <https://www.cartografia.servizirl.it/arcgis/rest/services/sirbec/BeniCulturaliVincolati/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: geologico
### 🟠 Mosaico della fattibilità
- Stato: **ENTRO_RAGGIO** · Tema: geologico · Norma: D.G.R. Lombardia IX/2616/2011 (classi di fattibilità 1-4)
- Fonte: Regione Lombardia – Mosaico della fattibilità geologica (Regione Lombardia)
  - CLASSE_FATTIBILITA=CLASSE 3; INFO_CLASSE_FATTIB=FATTIBILITA' CON CONSISTENTI LIMITAZIONI; ISTAT_COMUNE=017029; COMUNE=Brescia; BASE_RILIEVO=FOTOGRAMMETRICO; SCALA_RILIEVO=1:5000
  - CLASSE_FATTIBILITA=CLASSE 4; INFO_CLASSE_FATTIB=FATTIBILITA' CON GRAVI LIMITAZIONI; ISTAT_COMUNE=017029; COMUNE=Brescia; BASE_RILIEVO=FOTOGRAMMETRICO; SCALA_RILIEVO=1:5000
  - CLASSE_FATTIBILITA=CLASSE 2; INFO_CLASSE_FATTIB=FATTIBILITA' CON MODESTE LIMITAZIONI; ISTAT_COMUNE=017029; COMUNE=Brescia; BASE_RILIEVO=FOTOGRAMMETRICO; SCALA_RILIEVO=1:5000
  - CLASSE_FATTIBILITA=CLASSE 3; INFO_CLASSE_FATTIB=FATTIBILITA' CON CONSISTENTI LIMITAZIONI; ISTAT_COMUNE=017029; COMUNE=Brescia; BASE_RILIEVO=FOTOGRAMMETRICO; SCALA_RILIEVO=1:5000
  - CLASSE_FATTIBILITA=CLASSE 2; INFO_CLASSE_FATTIB=FATTIBILITA' CON MODESTE LIMITAZIONI; ISTAT_COMUNE=017029; COMUNE=Brescia; BASE_RILIEVO=FOTOGRAMMETRICO; SCALA_RILIEVO=1:5000
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale degli studi comunali; fa fede il PGT vigente.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/fattibilita_geologica/MapServer/88/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: idraulico
### 🟠 Corsi d’acqua del Reticolo Idrico Minore – RIM
- Stato: **ENTRO_RAGGIO** · Tema: idraulico · Norma: R.D. 523/1904; D.G.R. XII/3668/2024 (reticolo idrico)
- Fonte: Regione Lombardia – Reticolo idrico (RIP, RIB, RIM) (Regione Lombardia)
  - COD_RIM=03017029_0160
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Polizia idraulica: le fasce (di norma 10 m) si misurano dal ciglio/piede arginale, non dall'asse.
- Query (riproducibile, 2026-09-30T22:42:30+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/ReticoloIdrografico_RIRU/MapServer/7/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Reticolo Idrico di Bonifica – RIB Allegato C alla D.g.r. 16 dicembre 2024 n. XII/3668
- Stato: **ENTRO_RAGGIO** · Tema: idraulico · Norma: R.D. 523/1904; D.G.R. XII/3668/2024 (reticolo idrico)
- Fonte: Regione Lombardia – Reticolo idrico (RIP, RIB, RIM) (Regione Lombardia)
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6982; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6984; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6997; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=SCARICATORE N.1 VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6985; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6983; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6996; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6995; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6998; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
  - NOME_C_ACQ=VASO CELATO; TIPO_RETIC=BONIFICA; COD_RIB=6994; COMUNI=BRESCIA; FUNZIONE=PROMISCUO; GESTIONE=CONSORZIO DI BONIFICA OGLIO MELLA
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Polizia idraulica: le fasce (di norma 10 m) si misurano dal ciglio/piede arginale, non dall'asse.
- Query (riproducibile, 2026-09-30T22:42:30+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/ReticoloIdrografico_RIRU/MapServer/8/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: idrogeologico
### 🟠 Aree a franosità diffusa
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: Progetto IFFI (ISPRA/Regioni)
- Fonte: Regione Lombardia – Inventario fenomeni franosi (IFFI) (Regione Lombardia)
  - COD_TIPOMOVIMENTO=10; TIPOMOVIMENTO=AREE SOGGETTE A CROLLI/RIBALTAMENTI DIFFUSI; COD_TIPOFENOMENO=1; TIPOFENOMENO=FRANA; COD_STATO=2; STATO=ATTIVO/RIATTIVATO/SOSPESO
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:24+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/protciv/iffi/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Aree a pericolosità da frana PAI (mosaicatura)
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: PAI – L. 183/1989, D.L. 180/1998; D.Lgs. 152/2006
- Fonte: ISPRA – Mosaicatura PAI pericolosità da frana (ISPRA)
  - peric_ita=Elevata P3
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaicatura ISPRA armonizzata (P4-P1, AA): non sostituisce i PAI vigenti delle Autorità di bacino. Licenza CC-BY-SA 4.0.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sdi.isprambiente.it/geoserver/nz2/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=nz2%3Aaree_peric_frana_pai&outputFormat=application%2Fjson&count=20&CQL_FILTER=DWITHIN%28geom%2CSRID%3D4326%3BPOINT%2810.227873542813938+45.54667794588481%29%2C300.0%2Cmeters%29>
### 🟠 Aree franose
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: PTCP Brescia – Tav. 3.2
- Fonte: Provincia di Brescia – PTCP 2014: inventario dei dissesti (Provincia di Brescia)
  - legenda=Aree soggette a crolli/ribaltamenti diffusi
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:13+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_3_2_Inventario_dei_dissesti/MapServer/6/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Dissesti poligonali
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: PAI – L. 183/1989; Norme di Attuazione PAI (artt. 9, 29, 30, 31, 39)
- Fonte: Regione Lombardia – PAI vigente (dissesti e fasce fluviali) (Regione Lombardia)
  - NOME=Brescia; LEGENDA_PAI=112; DESCRIZIONE_LEGENDA=Area di frana quiescente (Fq)/Modifiche e integrazioni; ISTAT=017029
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Per le fasce fluviali fa fede il PAI vigente dell'Autorità di bacino.
- Query (riproducibile, 2026-09-30T22:42:23+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/pai_vigente/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Fattibilità classe 4
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: L.R. 12/2005 art. 57; PAI/PGRA
- Fonte: Provincia di Brescia – Difesa del suolo (Provincia di Brescia)
  - CLASSE_FAT=CLASSE 4; fonte=Regione Lombardia; aggiornamento=Ottobre 2023; ISTAT_COMU=017029; COMUNE=Brescia; INFO_CLASS=FATTIBILITA' CON GRAVI LIMITAZIONI
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:17+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/difesa_suolo/MapServer/5/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Frane
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: L.R. 12/2005 art. 57; PAI/PGRA
- Fonte: Provincia di Brescia – Difesa del suolo (Provincia di Brescia)
  - NOME=Brescia; LEGENDA_PA=112; DESCRIZION=Area di frana quiescente (Fq)/Modifiche e integrazioni; fonte=Regione Lombardia; aggiornamento=Ottobre 2023; ISTAT=017029
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:17+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/difesa_suolo/MapServer/11/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Punti storici
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: Progetto IFFI (ISPRA/Regioni)
- Fonte: Regione Lombardia – Inventario fenomeni franosi (IFFI) (Regione Lombardia)
  - COD_TIPOMOVIMENTO=10; TIPOMOVIMENTO=AREE SOGGETTE A CROLLI/RIBALTAMENTI DIFFUSI; COD_TIPOFENOMENO=1; TIPOFENOMENO=FRANA; COD_STATO=2; STATO=ATTIVO/RIATTIVATO/SOSPESO
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:24+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/protciv/iffi/MapServer/0/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 _Punto identificativo del fenomeno franoso
- Stato: **ENTRO_RAGGIO** · Tema: idrogeologico · Norma: PTCP Brescia – Tav. 3.2
- Fonte: Provincia di Brescia – PTCP 2014: inventario dei dissesti (Provincia di Brescia)
  - cod_tipo=9; cod_stato=100; data_oss=20000815000000; tipo=9; cod_reg=03
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:13+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_3_2_Inventario_dei_dissesti/MapServer/1/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: paesaggistico
### 🟠 Aree di notevole interesse pubblico
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Regione Lombardia – Vincoli paesaggistici (SIBA) (Regione Lombardia)
  - DATA_DEC=20/03/1958; DATA_COM=18/02/1957; DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; DORIG_DEC=Decreto Ministeriale; COD_DEC=19
  - DATA_DEC=30/10/1961; DATA_COM=20/11/1959; ART136_C1_LETT=c)d); DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; DORIG_DEC=Decreto Ministeriale; COD_DEC=131
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d19_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_19_Brescia.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d14_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_14_Brescia.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d131_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_131_Brescia.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Ricognitivo: verificare decreto/GU e cartografia originale.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/vincoli_paesaggistici/MapServer/14/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Bellezze d'insieme (D.Lgs. 42/2004 art. 136, comma 1, lettere c e d, e art. 157; ex L. 1497/39)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: PTCP Brescia (DCP 31/2014) – Tav. 2.7
- Fonte: Provincia di Brescia – PTCP 2014: tutele paesaggistiche (Provincia di Brescia)
  - immagini=https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d131_1.pdf; desc_decr2=Costalunga,  Brescia; conta=80; zz=mapsiba20/verbali_ba_siba/d131_1.pdf
  - immagini=https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d19_1.pdf; desc_decr2=Zona dei Ronchi, l'azienda Capretti e il Villaggio Pasotti, Brescia; conta=79; zz=mapsiba20/verbali_ba_siba/d19_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d131_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d19_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d14_1.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Replica provinciale di dati SIBA/PPR: utile come riscontro incrociato.
- Query (riproducibile, 2026-09-30T22:42:12+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_2_7_Tutele_paesaggistiche/MapServer/19/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Bellezze individue (D.Lgs. 42/2004 art. 136, comma 1, lettere a e b, e art. 157; ex L. 1497/85)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: PTCP Brescia (DCP 31/2014) – Tav. 2.7
- Fonte: Provincia di Brescia – PTCP 2014: tutele paesaggistiche (Provincia di Brescia)
  - nome_com=BRESCIA; descr_dec=bosco; immagini=https://www.cartografia.servizirl.it/mapsiba20/verbali_bi_siba/i236_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_bi_siba/i236_1.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Replica provinciale di dati SIBA/PPR: utile come riscontro incrociato.
- Query (riproducibile, 2026-09-30T22:42:10+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_2_7_Tutele_paesaggistiche/MapServer/5/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Beni e immobili di notevole interesse pubblico
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Regione Lombardia – Vincoli paesaggistici (SIBA) (Regione Lombardia)
  - DATA_DEC=25/10/1951; DESCR_DEC=bosco; DFONTE_BI=E' disponibile una fonte cartografica presso la Struttura Regionale competente; NOME_COM=BRESCIA; DORIG_DESC=Decreto Ministeriale; COD_DEC=236
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_bi_siba/i236_1.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Ricognitivo: verificare decreto/GU e cartografia originale.
- Query (riproducibile, 2026-09-30T22:42:20+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/vincoli_paesaggistici/MapServer/0/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Beni e immobili di notevole interesse pubblico (D.Lgs. 42/2004 art. 136, comma 1, lettere a e b, e art. 157)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004 (Provincia di Brescia)
  - NOME_COM=BRESCIA; DATA_DEC=25/10/1951; DESCR_DEC=bosco; FONTE_BI=120; DFONTE_BI=E' disponibile una fonte cartografica presso la Struttura Regionale competente; TIPO_CA=200
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/verbali_bi_siba/i236_1.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:18+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/dlgs42_2004/MapServer/8/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Centri e nuclei storici (PPR, art. 25)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: PTCP Brescia (DCP 31/2014) – Tav. 2.7
- Fonte: Provincia di Brescia – PTCP 2014: tutele paesaggistiche (Provincia di Brescia)
  - label=Centri e nuclei storici; ambito=II – ambiti di prevalente valore storico-culturale; sistema=e – sistema dei centri e nuclei urbani; elemento=II.e.1 - nuclei d'antica formazione
  - label=Centri e nuclei storici; ambito=II – ambiti di prevalente valore storico-culturale; sistema=e – sistema dei centri e nuclei urbani; elemento=II.e.1 - nuclei d'antica formazione
  - label=Centri e nuclei storici; ambito=II – ambiti di prevalente valore storico-culturale; sistema=e – sistema dei centri e nuclei urbani; elemento=II.e.1 - nuclei d'antica formazione
  - label=Centri e nuclei storici; ambito=II – ambiti di prevalente valore storico-culturale; sistema=e – sistema dei centri e nuclei urbani; elemento=II.e.1 - nuclei d'antica formazione
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Replica provinciale di dati SIBA/PPR: utile come riscontro incrociato.
- Query (riproducibile, 2026-09-30T22:42:12+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_2_7_Tutele_paesaggistiche/MapServer/37/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 I Longobardi in Italia. I luoghi del potere (568-774 d.C.)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: PPR Lombardia (norme di attuazione)
- Fonte: Regione Lombardia – Piano Paesaggistico Regionale (PPR) (Regione Lombardia)
  - TIPO_AREA=Buffer Zone; COD_UNESCO=1318; SITO=I Longobardi in Italia. I luoghi del potere (568-774 d.C.)
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Cartografia del PPR: prescrizioni da verificare nelle NdA.
- Query (riproducibile, 2026-09-30T22:42:22+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/piano_paesaggistico/MapServer/17/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Parchi Locali di Interesse Sovracomunale riconosciuti (LR 86/83)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: PTCP Brescia (DCP 31/2014) – Tav. 2.7
- Fonte: Provincia di Brescia – PTCP 2014: tutele paesaggistiche (Provincia di Brescia)
  - nome_plis=Parco delle Colline di Brescia
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Replica provinciale di dati SIBA/PPR: utile come riscontro incrociato.
- Query (riproducibile, 2026-09-30T22:42:12+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/ptcp_2014/tav_2_7_Tutele_paesaggistiche/MapServer/26/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Perimetro delle Aree di notevole interesse pubblico
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Regione Lombardia – Vincoli paesaggistici (SIBA) (Regione Lombardia)
  - DATA_DEC=20/03/1958; DATA_COM=18/02/1957; DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; DORIG_DEC=Decreto Ministeriale; COD_DEC=19
  - DATA_DEC=30/10/1961; DATA_COM=20/11/1959; ART136_C1_LETT=c)d); DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; DORIG_DEC=Decreto Ministeriale; COD_DEC=131
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d19_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_19_Brescia.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d14_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_14_Brescia.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/verbali_ba_siba/d131_1.pdf
  - Documento: https://www.cartografia.servizirl.it/mapsiba20/gu_ba_siba/GU_131_Brescia.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Ricognitivo: verificare decreto/GU e cartografia originale.
- Query (riproducibile, 2026-09-30T22:42:20+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/vincoli_paesaggistici/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Perimetro e Aree di notevole interesse pubblico (D.Lgs. 42/2004 art. 136, comma 1, lettere c e d, e art. 157)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004 (Provincia di Brescia)
  - DATA_DEC=20/03/1958; DATA_COM=18/02/1957; FONTE_BA=120; DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; TIPO_CA=200; DTIPO_CA=Cartografia catastale
  - DATA_DEC=30/10/1961; DATA_COM=20/11/1959; FONTE_BA=120; DFONTE_BA=E' disponibile una fonte cartografica presso la Struttura Regionale competente; TIPO_CA=202; DTIPO_CA=I.G.M.
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/verbali_ba_siba/d14_1.pdf
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/gu_ba_siba/GU_14_Brescia.pdf
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/verbali_ba_siba/d19_1.pdf
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/gu_ba_siba/GU_19_Brescia.pdf
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/verbali_ba_siba/d131_1.pdf
  - Documento: http://www.cartografia.regione.lombardia.it/mapsiba20/gu_ba_siba/GU_131_Brescia.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:18+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/dlgs42_2004/MapServer/4/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Territori coperti da foreste e da boschi
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Regione Lombardia – Vincoli paesaggistici (SIBA) (Regione Lombardia)
  - DESCRIZIONE=boschi di latifoglie a densità media e alta; CODICE=31111
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Ricognitivo: verificare decreto/GU e cartografia originale.
- Query (riproducibile, 2026-09-30T22:42:21+00:00): <https://www.cartografia.servizirl.it/arcgis2/rest/services/sistemiverdi/vincoli_paesaggistici/MapServer/12/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Territori coperti da foreste e da boschi (D.Lgs. 42/2004 art. 142, comma 1, lettera g)
- Stato: **ENTRO_RAGGIO** · Tema: paesaggistico · Norma: D.Lgs. 42/2004 artt. 136 e 142
- Fonte: Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004 (Provincia di Brescia)
  - DESCRIZION=boschi di latifoglie a densità media e alta; CODICE=31111
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:18+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/dlgs42_2004/MapServer/5/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: proprietà
### 🟠 particelle demanio
- Stato: **ENTRO_RAGGIO** · Tema: proprietà · Norma: Catasto – demanio
- Fonte: Regione Lombardia – Particelle demaniali (Regione Lombardia)
  - NOME_COMUN=BRESCIA; ID_PART=91070668; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=91070698; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=91070742; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=94297572; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=305255; DATA_ESTRA=31032021; DENOMINAZI=AZIENDA SOCIO SANITARIA TERRITORIALE DEGLI SPEDALI CIVILI DI BRESCIA; PART_IVA=03775110988; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=479186; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PART_IVA=00761890177; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=939246; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PART_IVA=00761890177; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=2475074; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PART_IVA=00761890177; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=3936899; DATA_ESTRA=31032021; DENOMINAZI=AZIENDA SOCIO SANITARIA TERRITORIALE DEGLI SPEDALI CIVILI DI BRESCIA; PART_IVA=03775110988; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=4985741; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PART_IVA=00761890177; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=5010968; DATA_ESTRA=31032021; DENOMINAZI=COMUNE DI BRESCIA; PART_IVA=00761890177; PROVINCIA=BRESCIA
  - NOME_COMUN=BRESCIA; ID_PART=5963881; DATA_ESTRA=31032021; DENOMINAZI=ISTITUTO SCOLASTICO - UNIVERSITA; PROVINCIA=BRESCIA
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:30+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/catasto_demanio/MapServer/10/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: protezione civile
### 🟠 Rete stradale
- Stato: **ENTRO_RAGGIO** · Tema: protezione civile · Norma: Piani di emergenza esterna (PEE)
- Fonte: Provincia di Brescia – Aree di piani di emergenza (dighe) (Provincia di Brescia)
  - sigla_stra=Strada comunale; nome_stra=Via Giovanni Lipella; comune=BRESCIA; gestore=Comune
  - sigla_stra=Strada comunale; nome_stra=Via Francesco Carini; comune=BRESCIA; gestore=Comune
  - sigla_stra=Strada comunale; nome_stra=Via Francesco Carini; comune=BRESCIA; gestore=Comune
  - sigla_stra=Strada comunale; nome_stra=Via Francesco Carini; comune=BRESCIA; gestore=Comune
- Nota: Elemento lineare/puntuale entro 25 m dal punto (non 'sul' punto): le fasce/distanze di rispetto si misurano secondo la norma specifica.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/protezione_civile/aree_pee/MapServer/8/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=25&units=esriSRUnit_Meter>
#### Tema: sismico
### 🟠 Aree stabili e aree stabili suscettibili di amplificazioni locali
- Stato: **ENTRO_RAGGIO** · Tema: sismico · Norma: OPCM 4007/2012; studi di microzonazione (livello 1)
- Fonte: Regione Lombardia – Microzonazione sismica (Regione Lombardia)
  - Tipo_z=1011; ID_z=27; URL=https://www.cartografia.servizirl.it/download/sismica/1011_017029.jpg; Comune=Brescia
  - Tipo_z=2003; ID_z=39; URL=https://www.cartografia.servizirl.it/download/sismica/2003_017029.jpg; Comune=Brescia
  - Documento: https://www.cartografia.servizirl.it/download/sismica/1011_017029.jpg
  - Documento: https://www.cartografia.servizirl.it/download/sismica/2008_017029.jpg
  - Documento: https://www.cartografia.servizirl.it/download/sismica/2003_017029.jpg
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/Microzonazione_sismica/MapServer/20/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Terreni di copertura e substrato geologico
- Stato: **ENTRO_RAGGIO** · Tema: sismico · Norma: OPCM 4007/2012; studi di microzonazione (livello 1)
- Fonte: Regione Lombardia – Microzonazione sismica (Regione Lombardia)
  - Tipo_gt=LPS; Stato=0; DESCR=Substrato geologico lapideo, stratificato; ID_gt=25; Comune=Brescia
  - Tipo_gt=GC; Stato=13; DESCR=Ghiaie argillose, miscela di ghiaia, sabbia e argilla; ID_gt=41; Gen=ca; Comune=Brescia
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/Microzonazione_sismica/MapServer/12/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Z4a - Zona di fondovalle con presenza di depositi alluvionali e/o fluvioglaciali granulari e/o coesivi
- Stato: **ENTRO_RAGGIO** · Tema: sismico · Norma: D.G.R. Lombardia IX/2616/2011 (componente sismica PGT)
- Fonte: Regione Lombardia – Pericolosità sismica locale (studi comunali) (Regione Lombardia)
  - SIGLA=Z4a; DESCRIZIONE=Zona di fondovalle con presenza di depositi alluvionali e/o fluvioglaciali granulari e/o coesivi; EFFETTI=AMPLIFICAZIONI LITOLOGICHE E GEOMETRICHE
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:26+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/pericolosita_sismica_locale/MapServer/105/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Z5 - Zona di contatto stratigrafico e/o tettonico tra litotipi con caratteristiche fisico-meccaniche molto diverse
- Stato: **ENTRO_RAGGIO** · Tema: sismico · Norma: D.G.R. Lombardia IX/2616/2011 (componente sismica PGT)
- Fonte: Regione Lombardia – Pericolosità sismica locale (studi comunali) (Regione Lombardia)
  - SIGLA=Z5; DESCRIZIONE=Zona di contatto stratigrafico e/o tettonico tra litotipi con caratteristiche fisico-meccaniche molto diverse; EFFETTI=COMPORTAMENTI DIFFERENZIALI
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:25+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/pericolosita_sismica_locale/MapServer/91/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: suolo e rifiuti
### 🟠 Vincoli aggregati
- Stato: **ENTRO_RAGGIO** · Tema: suolo e rifiuti · Norma: Piano provinciale rifiuti – criteri localizzativi impianti
- Fonte: Provincia di Brescia – Piano rifiuti: vincoli localizzativi aggregati (Provincia di Brescia)
  - tipo=Aree interessate da vincoli penalizzanti
  - tipo=Aree interessate da vincoli escludenti
  - tipo=Aree interessate da vincoli escludenti
  - tipo=Aree interessate da vincoli escludenti
  - tipo=Aree interessate da vincoli escludenti
  - tipo=Aree interessate da vincoli escludenti
  - tipo=Aree interessate da vincoli escludenti
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Vale per la localizzazione di impianti di gestione rifiuti, non come vincolo edilizio generale.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/rifiuti/R_12_carta_vincoli_aggregati_per_grado_prescrizione/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
#### Tema: urbanistico
### 🟠 Ambiti del tessuto urbano consolidato
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1513; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1514; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1515; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=697; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=698; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=699; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=700; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=701; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=702; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=703; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=704; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=705; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=706; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=707; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=708; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1314; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1315; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1316; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Nuclei Antichi Ring; AMB_URB=514; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Tessuti Storici; AMB_URB=410; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1219; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Tessuto prev. dest. resid. in ambito paes. amb.; AMB_URB=434; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Tessuti Storici; AMB_URB=435; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1224; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1225; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1226; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1040; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1041; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1042; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Tessuti Storici; AMB_URB=1044; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=1045; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Tessuti Storici; AMB_URB=1046; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=3317; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Tessuto prev. dest. resid. in ambito paes. amb.; AMB_URB=2784; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=3853; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=3854; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=4384; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=4710; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=3401; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=3897; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Residenziale; AMB_URB=3116; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=Tessuti Storici; AMB_URB=3130; COD_DEST1=100; DCOD_DEST1=RESIDENZIALE; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=4779; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=3468; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=4224; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=5960; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=6064; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=6065; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=servizi; AMB_URB=6522; COD_DEST1=105; DCOD_DEST1=SERVIZI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=infrastrutture trasporto; AMB_URB=6487; COD_DEST1=104; DCOD_DEST1=INFRASTRUTTURE DI TRASPORTO AREALI; SPEC_DEST=0
  - NOME_COM=BRESCIA; LEGENDA=residenziale commerciale MSV; AMB_URB=6165; COD_DEST1=102; DCOD_DEST1=TERZIARIO; SPEC_DEST=1
  - NOME_COM=BRESCIA; LEGENDA=residenziale commerciale MSV; AMB_URB=6166; COD_DEST1=102; DCOD_DEST1=TERZIARIO; SPEC_DEST=1
  - NOME_COM=BRESCIA; LEGENDA=residenziale commerciale MSV; AMB_URB=6167; COD_DEST1=102; DCOD_DEST1=TERZIARIO; SPEC_DEST=1
  - NOME_COM=BRESCIA; LEGENDA=residenziale commerciale MSV; AMB_URB=6168; COD_DEST1=102; DCOD_DEST1=TERZIARIO; SPEC_DEST=1
  - NOME_COM=BRESCIA; LEGENDA=residenziale commerciale MSV; AMB_URB=6169; COD_DEST1=102; DCOD_DEST1=TERZIARIO; SPEC_DEST=1
  - NOME_COM=BRESCIA; LEGENDA=residenziale commerciale MSV; AMB_URB=6170; COD_DEST1=102; DCOD_DEST1=TERZIARIO; SPEC_DEST=1
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_08.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_03.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_11.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_12.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_09.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_16.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20260506_AU_14.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:28+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/20/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Ambiti di trasformazione
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME_COM=BRESCIA; NOME_AMB=AT-E.2; AMB_TRAS=33; FUN_PREV1=105; DFUN_PREV1=SERVIZI; SPEC_DEST=0
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20251210_AT_33.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/13/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Aree supporto rete ecologica comunale
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME_COMUNE=BRESCIA; DATA_INIZIO=2022-03-16; COD_SUPPORTO=1797; NOTE=V2
  - NOME_COMUNE=BRESCIA; DATA_INIZIO=2022-03-16; COD_SUPPORTO=916; NOTE=V2
  - NOME_COMUNE=BRESCIA; DATA_INIZIO=2022-03-16; COD_SUPPORTO=990; NOTE=V1
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/7/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Azzonamenti comunali
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: Strumento urbanistico comunale
- Fonte: Regione Lombardia – Azzonamenti comunali (Regione Lombardia)
  - ARTICOLO=88; DESCRI_PRG=ZONA E2V2 AMBITI DI PIANURA DI RILEVANTE INTERESSE PAESISTICO E AMBIENTALE; COMUNE=BRESCIA; PRG=E2V2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=119; DESCRI_PRG=SPAZI SCOPERTI D'USO PUBBLICO - GIARDINI E PARCHI; COMUNE=BRESCIA; PRG=PV/VG
  - ARTICOLO=63; DESCRI_PRG=ZONA A2R1 CITTA' RESIDENZIALE - EDIFICI DA RISANARE; COMUNE=BRESCIA; PRG=A2R1
  - ARTICOLO=CART; DESCRI_PRG=SPAZI SCOPERTI D'USO PUBBLICO - PARCHEGGI A RASO; COMUNE=BRESCIA; PRG=PV/PP
  - ARTICOLO=76; DESCRI_PRG=ZONA B4R2 CITTA' RESIDENZIALE A DENSITA' MEDIA; COMUNE=BRESCIA; PRG=B4R2
  - ARTICOLO=76; DESCRI_PRG=ZONA B4R2 CITTA' RESIDENZIALE A DENSITA' MEDIA; COMUNE=BRESCIA; PRG=B4R2
  - ARTICOLO=CART; DESCRI_PRG=SERVIZI/ SERVIZI PER IL CULTO; COMUNE=BRESCIA; PRG=S/SF
  - ARTICOLO=CART; DESCRI_PRG=SERVIZI/ SCUOLA DI BASE; COMUNE=BRESCIA; PRG=S/SB
  - ARTICOLO=CART; DESCRI_PRG=SERVIZI/ SERVIZI AMMINISTRATIVI; COMUNE=BRESCIA; PRG=S/SE
  - ARTICOLO=CART; DESCRI_PRG=SERVIZI/ ISTRUZIONE SUPERIORE; COMUNE=BRESCIA; PRG=S/SI
  - ARTICOLO=93; DESCRI_PRG=PARCO DELLE COLLINE; COMUNE=BRESCIA; PRG=F2V1/P
  - ARTICOLO=93; DESCRI_PRG=PARCO DELLE COLLINE; COMUNE=BRESCIA; PRG=F2V1/P
  - ARTICOLO=89; DESCRI_PRG=ZONA E3V1 AMBITI COLLINARI E PEDECOLLINARI DI RILEVANTE INTERESSE PAESISTICO NATURALISTICO E AMBIENTALE; COMUNE=BRESCIA; PRG=E3V1
  - ARTICOLO=78; DESCRI_PRG=ZONA B5R2 CITTA' RESIDENZIALE A DENSITA' BASSA; COMUNE=BRESCIA; PRG=B5R2
  - ARTICOLO=CART; DESCRI_PRG=VINCOLO EX LEGE 490/99 ART. 139 - LETTERE A E B; COMUNE=BRESCIA; PRG=V490/99/AB
  - ARTICOLO=CART; DESCRI_PRG=SERVIZI/ SERVIZI OSPEDALIERI E SANITARI; COMUNE=BRESCIA; PRG=S/SH
  - ARTICOLO=CART; DESCRI_PRG=VIABILITA' ESISTENTE; COMUNE=BRESCIA; PRG=VIAB/E
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=78; DESCRI_PRG=ZONA B5R2 CITTA' RESIDENZIALE A DENSITA' BASSA; COMUNE=BRESCIA; PRG=B5R2
  - ARTICOLO=63; DESCRI_PRG=ZONA A2R1 CITTA' RESIDENZIALE - EDIFICI DA RISANARE; COMUNE=BRESCIA; PRG=A2R1
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=CART; DESCRI_PRG=VINCOLO DI ZONA A; COMUNE=BRESCIA; PRG=VINC/A
  - ARTICOLO=72; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A DENSITA' ALTA; COMUNE=BRESCIA; PRG=B2L2
  - ARTICOLO=CART; DESCRI_PRG=SERVIZI/ SERVIZI OSPEDALIERI E SANITARI; COMUNE=BRESCIA; PRG=S/SH
  - ARTICOLO=73; DESCRI_PRG=ZONA B3R2 CITTA' RESIDENZIALE A DENSITA' MEDIO ALTA; COMUNE=BRESCIA; PRG=B3R2
  - ARTICOLO=76; DESCRI_PRG=ZONA B4R2 CITTA' RESIDENZIALE A DENSITA' MEDIA; COMUNE=BRESCIA; PRG=B4R2
  - ARTICOLO=71; DESCRI_PRG=ZONA B1L2 LUOGHI A PREVALENTE DESTINAZIONE TERZIARIA A FORTE DENSITA'; COMUNE=BRESCIA; PRG=B1L2
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Zonizzazione di sintesi: può riferirsi a PRG/PGT non aggiornato; verificare il PGT vigente.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/Azzonamenti_comunali/MapServer/0/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Classi di sensibilità paesistica
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=5152; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=5168; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=7882; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=8846; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=5602; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=8322; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=8323; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=7746; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=7787; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=7788; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=5; DESCRIZION=SENSIBILITA' MOLTO ELEVATA; COD_SEN=7481; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4015; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4019; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4020; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4021; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4022; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4023; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4024; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4032; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4033; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3733; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3734; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3735; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3736; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3737; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3738; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3739; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3742; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3117; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4108; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4120; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4122; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4124; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3792; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3793; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4125; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4136; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4138; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=4180; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3207; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3219; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3220; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3842; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3232; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3233; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3866; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3868; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=2896; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3259; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3878; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3292; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3934; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3935; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3936; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - NOME_COM=BRESCIA; CLASSE=4; DESCRIZION=SENSIBILITA' ELEVATA; COD_SEN=3977; SCHEDA=https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
  - Documento: https://www.cartografia.servizirl.it/schede_pgt/017029/017029_20250102_SP_01.pdf
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:28+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/22/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Fattibilità geologica
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME=Brescia; DESCR_FATTIBILITA=Fattibilità con modeste limitazioni; NOME_COMUNE=BRESCIA
  - NOME=Brescia; DESCR_FATTIBILITA=Fattibilità con consistenti limitazioni; NOME_COMUNE=BRESCIA
  - NOME=Brescia; DESCR_FATTIBILITA=Fattibilità con gravi limitazioni; NOME_COMUNE=BRESCIA
  - NOME=Brescia; DESCR_FATTIBILITA=Fattibilità con modeste limitazioni; NOME_COMUNE=BRESCIA
  - NOME=Brescia; DESCR_FATTIBILITA=Fattibilità con consistenti limitazioni; NOME_COMUNE=BRESCIA
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/3/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Nodi rete ecologica comunale
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - TIPO_TUTELA=Plis, Parchi Locali di interesse sovra-comunali; NOME_COMUNE=BRESCIA; DATA_INIZIO=2025-01-02; COD_NODO=2; TUTELATO=Vero (Tutelato)
  - TIPO_TUTELA=Plis, Parchi Locali di interesse sovra-comunali; NOME_COMUNE=BRESCIA; DATA_INIZIO=2025-01-02; COD_NODO=5; TUTELATO=Vero (Tutelato)
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/8/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Nuclei di antica formazione
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME_COM=BRESCIA; COD_NUC=8
  - NOME_COM=BRESCIA; COD_NUC=18
  - NOME_COM=BRESCIA; COD_NUC=43
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/12/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Parchi locali - Dettaglio
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - NOME_CO=BRESCIA; NOME_ITER_PAL=Parco riconosciuto dalla Regione con piano approvato; DENOM_PAL=Parco delle Colline di Brescia; ITER_PAL=1
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/5/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Parchi locali riconosciuti
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - NOME_CO=BRESCIA; NOME_ITER_PAL=Parco riconosciuto dalla Regione con piano approvato; DENOM_PAL=Parco delle Colline di Brescia; ITER_PAL=1
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/4/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Pericolosità sismica lineare
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - TIPOLOGIA=Z5; DESCR_TIPOLOGIA=Zona di contatto stratigrafico e/o tettonico tra litotipi con caratteristiche fisico-meccaniche molto diverse; NOME=Brescia; DATA_INIZIO=2019-06-12
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/1/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Pericolosità sismica poligonale
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005 (PGT)
- Fonte: Regione Lombardia – Mosaico PGT (tavola delle previsioni) (Regione Lombardia)
  - NOME=Brescia; TIPOLOGIA=Z4a; DESCR_TIPOLOGIA=Zona di fondovalle con presenza di depositi alluvionali e/o fluvioglaciali granulari e/o coesivi; NOME_COMUNE=BRESCIA; DATA_INIZIO=2019-06-12
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico regionale dei PGT: dato trasmesso dai Comuni, può non riflettere l'ultima variante.
- Query (riproducibile, 2026-09-30T22:42:27+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/tav_previsioni_b/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Vincoli di P.R.G. - Aree di rispetto
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - (nessun attributo descrittivo)
  - (nessun attributo descrittivo)
  - (nessun attributo descrittivo)
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/12/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Vincoli di P.R.G. - Dettaglio
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - NOME_CO=BRESCIA; NOME_COD_VINC=Nuclei storici - Centro storico zona "A" (D.M. 1444/68 art. 2); NOME_VINC_PRINC=Nuclei storici; COD_VINC=11
  - NOME_CO=BRESCIA; NOME_COD_VINC=Zone sottoposte a tutela; NOME_VINC_PRINC=Aree a disciplina specifica di P.R.G.; COD_VINC=71
  - NOME_CO=BRESCIA; NOME_COD_VINC=Zone sottoposte a tutela; NOME_VINC_PRINC=Aree a disciplina specifica di P.R.G.; COD_VINC=71
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/14/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Vincoli di P.R.G. - Nuclei storici
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - NOME_CO=BRESCIA; NOME_COD_VINC=Nuclei storici - Centro storico zona "A" (D.M. 1444/68 art. 2); NOME_VINC_PRINC=Nuclei storici; COD_VINC=11
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/11/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 Vincoli di P.R.G. - Specifica di P.R.G
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: L.R. 12/2005; vincoli da PRG/PGT
- Fonte: Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli) (Regione Lombardia)
  - NOME_CO=BRESCIA; NOME_COD_VINC=Zone sottoposte a tutela; NOME_VINC_PRINC=Aree a disciplina specifica di P.R.G.; COD_VINC=71
  - NOME_CO=BRESCIA; NOME_COD_VINC=Zone sottoposte a tutela; NOME_VINC_PRINC=Aree a disciplina specifica di P.R.G.; COD_VINC=71
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Mosaico storico PRG/PGT: verificare sul PGT vigente del Comune.
- Query (riproducibile, 2026-09-30T22:42:29+00:00): <https://www.cartografia.servizirl.it/arcgis1/rest/services/territorio/mos_tav_b/MapServer/13/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>
### 🟠 mosaico PTCP 2014
- Stato: **ENTRO_RAGGIO** · Tema: urbanistico · Norma: PTCP Brescia – mosaico dei PGT
- Fonte: Provincia di Brescia – Mosaico PGT (ATO e destinazioni) (Provincia di Brescia)
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=102
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=402
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=402
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=452
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=452
  - stato=3; fonte=6; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=5; istat=17029; comune=BRESCIA; sus=1; cod_dest=403
  - stato=3; fonte=6; istat=17029; comune=BRESCIA; sus=1; cod_dest=401
  - stato=1; fonte=6; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=6; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=6; istat=17029; comune=BRESCIA; sus=1; cod_dest=100
  - stato=1; fonte=6; istat=17029; comune=BRESCIA; sus=1; cod_dest=401
- Nota: Non sul punto ma entro 300 m.
- Valore del dato: Dato ricognitivo: verificare l'atto originario e lo strumento vigente.
- Query (riproducibile, 2026-09-30T22:42:19+00:00): <https://sit.provincia.brescia.it/arcgis/rest/services/urbanistica/mosaico_PTCP_2014/MapServer/2/query?geometry=10.227873542813938%2C45.54667794588481&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json&distance=300.0&units=esriSRUnit_Meter>

## Da verificare manualmente (nessuna API)
#### Tema: culturale
### 📄 Vincoli in Rete (beni culturali vincolati)
- Stato: **VERIFICA_MANUALE** · Tema: culturale · Norma: D.Lgs. 42/2004 Parte II
- Fonte: Fonti documentali nazionali (vari)
  - Documento: https://www.vincoliinrete.beniculturali.it/VincoliInRete/vir/bene/ricercabeni
- Nota: Ricerca per comune/indirizzo; per un vincolo diretto serve identificare foglio e mappale catastale.
- Valore del dato: Consultazione a scopo conoscitivo.
- Link: https://www.vincoliinrete.beniculturali.it/VincoliInRete/vir/bene/ricercabeni
#### Tema: multi-tema
### 📄 Interroga il territorio e il Paesaggio (report PDF multilivello)
- Stato: **VERIFICA_MANUALE** · Tema: multi-tema
- Fonte: Fonti documentali Regione Lombardia (Regione Lombardia)
  - Documento: https://www.geoportale.regione.lombardia.it/news/-/asset_publisher/80SRILUddraK/content/interroga-il-territorio
- Nota: Interrogazione puntuale con report PDF; dichiaratamente ricognitivo e non certificativo.
- Link: https://www.geoportale.regione.lombardia.it/news/-/asset_publisher/80SRILUddraK/content/interroga-il-territorio
#### Tema: paesaggistico
### 📄 Tavola PGT vincoli paesaggistici (SIT Provincia di Brescia)
- Stato: **VERIFICA_MANUALE** · Tema: paesaggistico
- Fonte: Fonti documentali Comune di Brescia (Comune di Brescia)
  - Documento: https://sit.provincia.brescia.it/tavola/pgt-vincoli-paesaggistici
- Nota: Cartografia di consultazione.
- Link: https://sit.provincia.brescia.it/tavola/pgt-vincoli-paesaggistici
#### Tema: urbanistico
### 📄 Certificato di Destinazione Urbanistica (CDU)
- Stato: **VERIFICA_MANUALE** · Tema: urbanistico · Norma: DPR 380/2001 art. 30
- Fonte: Fonti documentali nazionali (vari)
- Nota: Unico documento con valore certificativo sulle prescrizioni urbanistiche; si richiede al Comune indicando foglio e mappale.
- Valore del dato: Valore certificativo.
### 📄 Certificazioni urbanistiche (CDU) del Comune
- Stato: **VERIFICA_MANUALE** · Tema: urbanistico · Norma: DPR 380/2001 art. 30
- Fonte: Fonti documentali Comune di Brescia (Comune di Brescia)
  - Documento: https://www.comune.brescia.it/it/servizi/certificazioni-urbanistiche
- Nota: Richiesta online del CDU; requisiti, costi e tempi vanno verificati sulla pagina ufficiale (possono variare).
- Valore del dato: Valore certificativo.
- Link: https://www.comune.brescia.it/it/servizi/certificazioni-urbanistiche
### 📄 PGT vigente (Piano delle Regole, Documento di Piano, Piano dei Servizi, NTA)
- Stato: **VERIFICA_MANUALE** · Tema: urbanistico
- Fonte: Fonti documentali Comune di Brescia (Comune di Brescia)
  - Documento: https://www.comune.brescia.it/aree-tematiche/urbanistica/piano-di-governo-del-territorio/pgt-vigente
- Nota: Consultare le tavole dei vincoli, della fattibilità geologica e del reticolo idrico; non certificativo.
- Link: https://www.comune.brescia.it/aree-tematiche/urbanistica/piano-di-governo-del-territorio/pgt-vigente

## Livelli interrogati senza elementi sul punto
- Pozzi — Provincia di Brescia – Pozzi e aree di rispetto
- _#pozzi — Provincia di Brescia – Pozzi e aree di rispetto
- #Ambiti estrattivi — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- #Ambiti estrattivi — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Aeroporti esistenti — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Alpeggi — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Ambiti ad elevata naturalità (PPR art. 17) — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Ambiti destinati all'attività agricola di interesse strategico (AAS) — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Ambiti di valore paesistico ambientale — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Ambiti estrattivi — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Areale A - PTRA Montichiari — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Controdeduzioni osservazione n° 345/2014/140/1 — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Ecosistemi acquatici (DUSAF) — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Fermate metropolitana — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Interscambi tra rete della viabilità e sistemi di trasporto pubblico — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Nodi logistici di livello sovra-provinciale; Nodi logistici di livello locale — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Nodo del trasporto pubblico — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Reticolo idrico principale ai fini della polizia idraulica — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Riserve naturali — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Stazioni ferroviarie — Provincia di Brescia – PTCP 2014: ambiti agricoli strategici
- Ambiti dei fontanili — Provincia di Brescia – PTCP 2014: rete ecologica
- Ambiti dei fontanili — Provincia di Brescia – Carta dei vincoli (PTCP)
- Ambiti di consolidamento ecologico delle colline moreniche del Garda — Provincia di Brescia – PTCP 2014: rete ecologica
- Ambiti di consolidamento ecologico delle colline moreniche del Garda — Provincia di Brescia – Carta dei vincoli (PTCP)
- Aree a convenzione Ramsar — Regione Lombardia – Aree protette
- Aree ad elevato valore naturalistico — Provincia di Brescia – PTCP 2014: rete ecologica
- Aree ad elevato valore naturalistico — Provincia di Brescia – Carta dei vincoli (PTCP)
- Aree designate a livello nazionale (CDDA) — EEA – Aree protette nazionali (CDDA v21)
- Aree naturali di completamento — Provincia di Brescia – PTCP 2014: rete ecologica
- Aree naturali di completamento — Provincia di Brescia – Carta dei vincoli (PTCP)
- Aree per la ricostruzione polivalente dell'agroecosistema — Provincia di Brescia – PTCP 2014: rete ecologica
- Aree per la ricostruzione polivalente dell'agroecosistema — Provincia di Brescia – Carta dei vincoli (PTCP)
- Aree problematiche all'interno dei corridoi ecologici — Provincia di Brescia – PTCP 2014: rete ecologica
- Aree problematiche all'interno dei corridoi ecologici — Provincia di Brescia – Carta dei vincoli (PTCP)
- Corridoi ecologici — Provincia di Brescia – PTCP 2014: rete ecologica
- Corridoi ecologici — Provincia di Brescia – Carta dei vincoli (PTCP)
- Corridoi ecologici primari — Provincia di Brescia – PTCP 2014: rete ecologica
- Corridoi ecologici primari — Provincia di Brescia – Carta dei vincoli (PTCP)
- Direttrici di collegamento esterno — Provincia di Brescia – PTCP 2014: rete ecologica
- Direttrici di collegamento esterno — Provincia di Brescia – Carta dei vincoli (PTCP)
- ELEMENTI DI PRIMO LIVELLO DELLA RER — Regione Lombardia – Rete Ecologica Regionale
- ELEMENTI DI SECONDO LIVELLO DELLA RER — Regione Lombardia – Rete Ecologica Regionale
- Elementi di primo livello della RER — Provincia di Brescia – PTCP 2014: rete ecologica
- Elementi di primo livello della RER — Provincia di Brescia – Carta dei vincoli (PTCP)
- Ferrovia Alta velocità/Alta capacità (AV/AC) — Provincia di Brescia – Carta dei vincoli (PTCP)
- Fronti problematici all'interno dei corridoi ecologici — Provincia di Brescia – PTCP 2014: rete ecologica
- Fronti problematici all'interno dei corridoi ecologici — Provincia di Brescia – Carta dei vincoli (PTCP)
- Habitat Natura 2000 — Regione Lombardia – Rete Natura 2000
- Linee ferroviarie metropolitane — Provincia di Brescia – Carta dei vincoli (PTCP)
- Linee ferroviarie storiche (Linee S) — Provincia di Brescia – Carta dei vincoli (PTCP)
- Metropolitana — Provincia di Brescia – Carta dei vincoli (PTCP)
- Monumenti naturali - poligonali — Regione Lombardia – Aree protette
- Monumenti naturali - puntuali — Regione Lombardia – Aree protette
- PERIMETRI ATE — Provincia di Brescia – Carta dei vincoli (PTCP)
- Parchi locali di interesse sovracomunale — Regione Lombardia – Aree protette
- Parchi naturali — Regione Lombardia – Aree protette
- Parchi nazionali — Regione Lombardia – Aree protette
- Parchi regionali — Regione Lombardia – Aree protette
- Parchi regionali nazionali — Provincia di Brescia – PTCP 2014: rete ecologica
- Parchi regionali nazionali — Provincia di Brescia – Carta dei vincoli (PTCP)
- Principali ecosistemi lacustri — Provincia di Brescia – PTCP 2014: rete ecologica
- Principali ecosistemi lacustri — Provincia di Brescia – Carta dei vincoli (PTCP)
- Principali punti di conflitto della rete con le infrastrutture prioritarie — Provincia di Brescia – PTCP 2014: rete ecologica
- Principali punti di conflitto della rete con le infrastrutture prioritarie — Provincia di Brescia – Carta dei vincoli (PTCP)
- Rete Natura 2000 (SIC) — Provincia di Brescia – PTCP 2014: rete ecologica
- Rete Natura 2000 (SIC) — Provincia di Brescia – Carta dei vincoli (PTCP)
- Rete Natura 2000 (ZPS) — Provincia di Brescia – PTCP 2014: rete ecologica
- Rete Natura 2000 (ZPS) — Provincia di Brescia – Carta dei vincoli (PTCP)
- Rete della viabilità locale — Provincia di Brescia – Carta dei vincoli (PTCP)
- Rete viaria — Provincia di Brescia – Carta dei vincoli (PTCP)
- Reticolo idrico principale — Provincia di Brescia – PTCP 2014: rete ecologica
- Reticolo idrico principale — Provincia di Brescia – Carta dei vincoli (PTCP)
- Riserve naturali nazionali — Regione Lombardia – Aree protette
- Riserve naturali regionali — Regione Lombardia – Aree protette
- Siti Direttiva Habitat (pSCI/SCI/ZSC) — EEA – Rete Natura 2000
- Siti Direttiva Uccelli (ZPS) — EEA – Rete Natura 2000
- Siti Habitat e Uccelli — EEA – Rete Natura 2000
- Varchi REP — Provincia di Brescia – PTCP 2014: rete ecologica
- Varchi REP — Provincia di Brescia – Carta dei vincoli (PTCP)
- Varchi RER — Provincia di Brescia – PTCP 2014: rete ecologica
- Varchi RER — Provincia di Brescia – Carta dei vincoli (PTCP)
- Zone di protezione speciale (ZPS) — Regione Lombardia – Rete Natura 2000
- Zone speciali di conservazione e Siti di Importanza Comunitaria (ZSC e SIC) — Regione Lombardia – Rete Natura 2000
- Zone umide — Provincia di Brescia – PTCP 2014: rete ecologica
- Zone umide — Provincia di Brescia – Carta dei vincoli (PTCP)
- _#Confini comunali — Provincia di Brescia – PTCP 2014: rete ecologica
- Zona omogenea allerta valanghe — Regione Lombardia – Attestato del territorio (contesto)
- Edificio segnalato TCI — Regione Lombardia – Beni culturali vincolati (SIRBeC)
- Edificio vincolato — Regione Lombardia – Beni culturali vincolati (SIRBeC)
- Edificio vincolato e segnalato TCI — Regione Lombardia – Beni culturali vincolati (SIRBeC)
- Aree percorse 1997-2021 — Provincia di Brescia – Aree percorse dal fuoco
- Boschi NON TRASFORMABILI — Provincia di Brescia – PIF: trasformabilità del bosco
- Boschi di protezione — Regione Lombardia – Boschi di protezione
- Boschi trasformabili per PUBBLICA UTILITA' — Provincia di Brescia – PIF: trasformabilità del bosco
- Carta di governo del bosco — Regione Lombardia – Foreste (governo, destinazioni, piani di assestamento)
- Destinazioni selvicolturali — Regione Lombardia – Destinazioni selvicolturali
- Perimetro esterno del Piano di Assestamento Forestale (PAF) 2025 — Regione Lombardia – Piani di assestamento forestale
- Rapporto di compensazione — Provincia di Brescia – PIF: trasformabilità del bosco
- Vincoli — Provincia di Brescia – PIF: trasformabilità del bosco
- Aree Allagabili Tergo Bpr 2020 — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- Corsi d’acqua del Reticolo Idrico Minore – RIM — Regione Lombardia – Reticolo idrico (RIP, RIB, RIM)
- Dir. alluvioni - Aree allagabili aree costiere lacuali — Regione Lombardia – PGRA aree allagabili (attestato del territorio)
- Dir. alluvioni - Aree allagabili sul ret. sec. collinare e mont. — Regione Lombardia – PGRA aree allagabili (attestato del territorio)
- Dir. alluvioni - Aree allagabili sul ret. secondario di pianura — Regione Lombardia – PGRA aree allagabili (attestato del territorio)
- Dir. alluvioni - Aree allagabili sul reticolo principale — Regione Lombardia – PGRA aree allagabili (attestato del territorio)
- PGRA Aree allagabili – Scenario di pericolosità Poco frequente (M) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità Poco frequente (M) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità Poco frequente (M) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità Poco frequente (M) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità frequente (H) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità frequente (H) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità frequente (H) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità frequente (H) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità raro (L) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità raro (L) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- PGRA Aree allagabili – Scenario di pericolosità raro (L) — Provincia di Brescia – PGRA aree allagabili (PTCP, agg. 2025)
- Reticolo Idrico Principale RIP - Allegato A alla D.g.r. 16 dicembre 2024 n. XII/3668 — Regione Lombardia – Reticolo idrico (RIP, RIB, RIM)
- Reticolo Idrico Principale di competenza AIPO Allegato B alla D.g.r. 16 dicembre 2024 n. XII/3668 — Regione Lombardia – Reticolo idrico (RIP, RIB, RIM)
- Reticolo Idrico di Bonifica – RIB Allegato C alla D.g.r. 16 dicembre 2024 n. XII/3668 — Regione Lombardia – Reticolo idrico (RIP, RIB, RIM)
- Ambito Servizio di piena (dgr 3723 del 19/06/2015) — Regione Lombardia – Attestato del territorio (vincolo idrogeologico, difesa del suolo)
- Ambito presidio idraulico (dgr 3723 del 19/06/2015) — Regione Lombardia – Attestato del territorio (vincolo idrogeologico, difesa del suolo)
- Ambito presidio idrogeol. (dgr 3723 del 19/06/2015) — Regione Lombardia – Attestato del territorio (vincolo idrogeologico, difesa del suolo)
- Aree Allagabili tergo B di progetto — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Aree RME vigenti — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Aree Umide della pianura bresciana e degli anfiteatri morenici — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Aree a franosità diffusa — Regione Lombardia – Inventario fenomeni franosi (IFFI)
- Aree a pericolosità da frana PAI (mosaicatura) — ISPRA – Mosaicatura PAI pericolosità da frana
- Aree a rischio idrogeologico molto elevato — Provincia di Brescia – Difesa del suolo
- Aree a rischio idrogeologico molto elevato 267/98 — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Aree a vulnerabilita` estremamente alta delle acque sotterranee per la presenza di circuiti idrici di tipo carsico ben sviluppati — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Aree di cui all'art. 9 NTA P.A.I — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Aree franose — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- Bacini idrici — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Concessioni Acque Minerali Termali — Provincia di Brescia – Difesa del suolo
- Conoidi — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- Conoidi detritico-alluvionali — Regione Lombardia – Inventario fenomeni franosi (IFFI)
- DGPV - Deformazioni Gravitative Profonde di Versante — Regione Lombardia – Inventario fenomeni franosi (IFFI)
- DGPV - Deformazioni gravitative profonde — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- Dissesti di dimensioni non cartografabili — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Dissesti lineari — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Dissesti lineari — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Dissesti poligonali — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Dissesti puntuali — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Esondazioni e dissesti morfologici di carattere torrentizio lungo le aste dei corsi d'acqua — Provincia di Brescia – Difesa del suolo
- Fasce PAI — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Fasce PAI (lineari) — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Fattibilità classe 4 — Provincia di Brescia – Difesa del suolo
- Fiumi afferenti ai laghi per un tratto di 10 km — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Fontanili — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Frane — Provincia di Brescia – Difesa del suolo
- Frane lineari — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- Frane lineari — Regione Lombardia – Inventario fenomeni franosi (IFFI)
- Frane poligonali — Regione Lombardia – Inventario fenomeni franosi (IFFI)
- Geositi — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Ghiacciai e nevai perenni — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Limite Fascia A — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Limite Fascia B — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Limite Fascia B di progetto — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- Limite Fascia C — Regione Lombardia – PAI vigente (dissesti e fasce fluviali)
- PAI – Fascia fluviale A — Provincia di Brescia – Difesa del suolo
- PAI – Fascia fluviale B — Provincia di Brescia – Difesa del suolo
- PAI – Fascia fluviale C — Provincia di Brescia – Difesa del suolo
- PGRA Aree allagabili – Scenario di pericolosità Poco frequente (M) — Provincia di Brescia – Difesa del suolo
- PGRA Aree allagabili – Scenario di pericolosità frequente (H) — Provincia di Brescia – Difesa del suolo
- PGRA Aree allagabili – Scenario di pericolosità raro (L) — Provincia di Brescia – Difesa del suolo
- Pericolo localizzato da rilevamento — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- Pozzi — Provincia di Brescia – Difesa del suolo
- Pozzi e sorgenti — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Punti storici — Regione Lombardia – Inventario fenomeni franosi (IFFI)
- Reticolo idrografico principale — Provincia di Brescia – PTCP 2014: ambiente e rischi
- Scheda valanghe — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- Siti valanghivi da rilevamento — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- Sito contaminato — Provincia di Brescia – Difesa del suolo
- Sorgenti — Provincia di Brescia – Difesa del suolo
- Trasporti in massa sui conoidi — Provincia di Brescia – Difesa del suolo
- Valanghe — Provincia di Brescia – Difesa del suolo
- Valanghe da fotointerpretazione — Regione Lombardia – Attestato del territorio (vincolo idrogeologico, difesa del suolo)
- Valanghe da rilevamento — Regione Lombardia – Attestato del territorio (vincolo idrogeologico, difesa del suolo)
- Vincolo idrogeologico — Provincia di Brescia – Vincolo idrogeologico
- Vincolo idrogeologico — Regione Lombardia – Attestato del territorio (vincolo idrogeologico, difesa del suolo)
- Vulnerabilità alta e molto alta della falda — Provincia di Brescia – PTCP 2014: ambiente e rischi
- _Punto identificativo del fenomeno franoso — Provincia di Brescia – PTCP 2014: inventario dei dissesti
- dissesti_lineari — Provincia di Brescia – Difesa del suolo
- pai_dissesti — Provincia di Brescia – Difesa del suolo
- #_Fiumi torrenti e corsi d'acqua pubblici e relative sponde (D.Lgs. 42/2004 art. 142, comma 1, lettera c; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Alvei fluviali tutelati — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Ambiti ad elevata naturalità (PPR, art 17) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Ambiti di criticità (PPR, Indirizzi di tutela - Parte III) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Ambiti di elevata naturalita' della montagna - [art. 17] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Ambiti di specifico valore storico ambietale Barco della Certosa - [art. 18] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Ambiti di tutela dello scenario lacuale  (PPR, art. 19) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Ambito di salvaguardia dello scenario lacuale- art. 19-c4 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Ambito di specifica tutela  dei laghi di Mantova  - art. 19-c2 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Ambito di specifica tutela  dei laghi insubrici - art. 19-c5 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Ambito di specifica tutela paesaggistica del fiume Po - [art. 20, comma 8] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Ambito di tutela paesaggistica del sistema vallivo del fiume Po - [art.20, comma 9] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Area argini maestri fiume Po — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Aree di interesse pubblico di difficile cartografazione — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Aree rispetto corsi d’acqua tutelati — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Arte rupestre della Valle Camonica — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Bellezze individue (D.Lgs. 42/2004 art. 136, comma 1, lettere a e b, e art. 157; ex L. 1497/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Belvedere - [art. 27, comma2] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Belvedere del paesaggio lombardo (art. 27 c. 4 PPR) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Beni di interesse archeologico (D.Lgs. 42/2004 art. 10) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Beni di interesse storico-architettonico (D.Lgs. 42/2004 art. 10 e 116) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Beni di interesse storico-architettonico (D.Lgs. 42/2004 art. 10 e 116; ex L. 1089/39) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Beni e immobili di notevole interesse pubblico — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Beni e immobili di notevole interesse pubblico (D.Lgs. 42/2004 art. 136, comma 1, lettere a e b, e art. 157) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Beni interesse archeologico (D.Lgs. 42/2004 ar. 10; ex L. 1089/39) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Buffer zone - Parchi d'arte rupestre Valle Camonica — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Buffer zone - Siti archeologici — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Centri e nuclei storici (PPR, art. 25) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Crespi d'Adda — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Fiumi torrenti e corsi acqua pubblici e relative sponde (D.Lgs. 42/2004 art. 142, comma 1, lettera c) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Fiumi torrenti e corsi d'acqua pubblici e relative sponde (D.Lgs. 42/2004 art. 142, comma 1, lettera c; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Fiumi, torrenti e corsi d'acqua pubblici e relative sponde — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Foreste e boschi (D.Lgs. 42/2004 art. 142, comma 1, lettera g; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Geositi (PPR, art. 22) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Geositi di interesse geografico, geomorfologico, paesistico, naturalistico-art.22-c4 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Geositi di interesse geologico-stratigrafico/strutturale, geominerario-art.22-c3 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Geositi di interesse paleontologico, paleoantropologico e mineralogico-art.22-c5 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Ghiacciai (D.Lgs. 42/2004 art. 142, comma 1, lettera e; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Ghiacciai e circhi glaciali — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Ghiacciai e circhi glaciali (D.Lgs. 42/2004 art. 142, comma 1, lettera e) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- I Longobardi in Italia. I luoghi del potere (568-774 d.C.) — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Il Naviglio Grande e il Naviglio di Pavia - [art. 21, comma 3] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Infrastruttura idrografica artificiale della pianura (PPR, art 21, cc.4-5-6) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- La Chiesa e il Convento Domenicano di Santa Maria Delle Grazie e il 'Cenacolo' di Leonardo Da Vinci — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- La ferrovia retica nel paesaggio dell'Albula e del Bernina — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Laghi (PPR, art. 19) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Le opere di difesa veneziane tra il XVI e XVII secolo: Stato da Terra – Stato da Mar Occidentale — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Mantova e Sabbioneta — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Monte San Giorgio — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Monumenti naturali — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Monumenti naturali — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Naviglio Martesana - [art. 21, comma 4] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Oltrepo Pavese –art. 22-c7 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Parchi Locali di Interesse Sovracomunale riconosciuti (LR 86/83) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Parchi archeologici (D.Lgs. 42/2004 art. 142, comma 1, lettera m) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Parchi archeologici (D.Lgs. 42/2004 art. 142, comma 1, lettera m; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Parchi d'arte rupestre della Valle Camonica - SITO  UNESCO N° 94 — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Parchi naturali istituiti (L. 394/91) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Parchi nazionali e regionali — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Parchi regionali ((D.Lgs. 42/2004 art. 142, comma 1 lettera f; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Parchi regionali nazionali (D.Lgs. 42/2004 art. 142, comma 1 lettera f) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Principali Navigli storici e canali art.21-c5 — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Punti di osservazione del paesaggio lombardo (art. 27 c. 4 PPR) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Punti di osservazione del paesaggio lombardo - [art. 27, comma4] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Riserve nazionali e regionali — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Riserve regionali nazionali (D.Lgs. 42/2004 art. 142, comma 1, lettera f) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Riseve regionali (D.Lgs. 42/2004 art. 142, comma 1, lettera f; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Sacri Monti di Piemonte e Lombardia — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Siti Unesco — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Siti di interesse comunitario (SIC - Direttiva 92/43/CEE "Habitat") — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Siti palafitticoli preistorici dell'arco alpino — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Siti palafitticoli preistorici dell'arco alpino — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Sponde Fiumi torrenti e corsi acqua pubblici (D.Lgs. 42/2004 art. 142, comma 1, lettera c) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Sponde Fiumi torrenti e corsi acqua pubblici (D.Lgs. 42/2004 art. 142, comma 1, lettera c) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Strade Panoramiche — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Terreni alpini e appenninici — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Territori alpini e appenninici (D.Lgs. 42/2004 art. 142, comma 1, lettera d) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Territori alpini ed appenninici (D.Lgs. 42/2004 art. 142, comma 1, lettera d; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Territori contermini a i laghi — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Territori contermini ai laghi (D.Lgs. 42/2004 art. 142, comma 1, lettera b) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Territori contermini ai laghi (D.Lgs. 42/2004 art. 142, comma 1, lettera b; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Territori coperti da foreste e da boschi — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Territori coperti da foreste e da boschi (D.Lgs. 42/2004 art. 142, comma 1, lettera g) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Tracciati guida paesaggistici — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Visuali sensibili - [art. 27, comma3] — Regione Lombardia – Piano Paesaggistico Regionale (PPR)
- Visuali sensibili del paesaggio lombardo (art. 27 c. 4 PPR) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Zone di protezione speciale (ZPS - Direttiva 79/409/CEE "Uccelli) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- Zone umide — Regione Lombardia – Vincoli paesaggistici (SIBA)
- Zone umide (D.Lgs. 42/2004 art. 142, comma 1, lettera i) — Provincia di Brescia – Beni paesaggistici D.Lgs. 42/2004
- Zone umide (D.Lgs. 42/2004 art. 142, comma 1, lettera i; ex L. 431/85) — Provincia di Brescia – PTCP 2014: tutele paesaggistiche
- particelle demanio — Regione Lombardia – Particelle demaniali
- Aree attenzione PEE approvati — Provincia di Brescia – Aree di piani di emergenza (dighe)
- Cippi stradali Chilometrici — Provincia di Brescia – Aree di piani di emergenza (dighe)
- Cippi stradali Ettometrici — Provincia di Brescia – Aree di piani di emergenza (dighe)
- Cippi stradali Virtuali — Provincia di Brescia – Aree di piani di emergenza (dighe)
- Cippi stradali svincoli — Provincia di Brescia – Aree di piani di emergenza (dighe)
- Impianti rifiuti : in aggiornamento — Provincia di Brescia – Aree di piani di emergenza (dighe)
- Manufatti ponti — Provincia di Brescia – Aree di piani di emergenza (dighe)
- PEE Ditte Rifiuti — Provincia di Brescia – Aree di piani di emergenza (dighe)
- Perimetri PEE approvati — Provincia di Brescia – Aree di piani di emergenza (dighe)
- NV — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- NV — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z1a - Zona caratterizzata da movimenti franosi attivi — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z1b - Zona caratterizzata da movimenti franosi quiescenti — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z1c - Zona potenzialmente franosa o esposta a rischio di frana — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z2a - Zone con terreni di fondazione saturi particolarmente scadenti — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z2b - Zona con terreni di fondazione particolarmente scadenti — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z3a - Zona di ciglio H>10m — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z3a - Zona di ciglio H>10m — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z3b - Zona di cresta rocciosa e/o cocuzzolo — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z3b - Zona di cresta rocciosa e/o cocuzzolo — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z4a - Zona di fondovalle con presenza di depositi alluvionali e/o fluvioglaciali granulari e/o coesivi — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z4c - Zona morenica con presenza di depositi granulari e/o coesivi — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z4d - Zona con presenza di argille residuali e terre rosse di origine pluvio-colluviale — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z5 - Zona di contatto stratigrafico e/o tettonico tra litotipi con caratteristiche fisico-meccaniche molto diverse — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- Z5 - Zona di contatto stratigrafico e/o tettonico tra litotipi con caratteristiche fisico-meccaniche molto diverse — Regione Lombardia – Pericolosità sismica locale (studi comunali)
- ATE calcari versione precedente — Provincia di Brescia – Ambiti territoriali estrattivi (ATE)
- Settore Argilla (2000-2013) — Provincia di Brescia – Ambiti territoriali estrattivi (ATE)
- Settore Calcari (vigente) — Provincia di Brescia – Ambiti territoriali estrattivi (ATE)
- Settore Pietre Ornamentali e Pietrischi (vigente) — Provincia di Brescia – Ambiti territoriali estrattivi (ATE)
- Settore Sabbia-Ghiaia e Argilla (vigente) — Provincia di Brescia – Ambiti territoriali estrattivi (ATE)
- Siti Bonificati in Lombardia — Regione Lombardia – Siti contaminati e bonificati
- Siti Contaminati e Bonificati — Regione Lombardia – Siti contaminati e bonificati
- Siti Contaminati in Lombardia — Regione Lombardia – Siti contaminati e bonificati
- Ambiti di rigenerazione urbana e territoriale — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Ambiti di trasformazione — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Aree agricole — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Aree di valore paesaggistico-ambientale ed ecologico — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Aree di valore paesaggistico-ambientale ed ecologico puntuali — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Aree dismesse, abbandonate, degradate — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Aree supporto rete ecologica comunale — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Fasce di rispetto cimiteriali — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Fasce di rispetto da impianti di depurazione — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Fasce di rispetto da pozzi e sorgenti — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Fasce di rispetto ferroviario — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Fasce di rispetto stradale — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Limitazioni in aree limitrofe ad aeroporti — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Limitazioni per servitù militari — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Nodi rete ecologica comunale — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Nuclei di antica formazione — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Parchi locali - Dettaglio — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Parchi locali istituiti — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Parchi locali riconosciuti — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Pericolosità sismica lineare — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Varchi rete ecologica comunale — Regione Lombardia – Mosaico PGT (tavola delle previsioni)
- Vincoli - Aree a servitu' speciali — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Vincoli di P.R.G. - Dettaglio — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Vincoli di P.R.G. - Nuclei storici — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Vincoli di P.R.G. - Specifica di P.R.G — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Vincoli legge 431/85 — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Vincolo L. 1089/39 — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
- Vincolo idreogeologico — Regione Lombardia – Mosaico PGT/PRG (tavola dei vincoli)
