@echo off
REM Avvia l'interfaccia grafica di ricerca preventivi
cd /d "%~dp0"
python gui.py
if errorlevel 1 pause
