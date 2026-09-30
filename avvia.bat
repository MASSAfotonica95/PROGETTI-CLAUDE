@echo off
rem Avvia la versione web locale (richiede Python 3.9+, nessun pacchetto aggiuntivo)
py -m vincoli.webapp || python -m vincoli.webapp
pause
