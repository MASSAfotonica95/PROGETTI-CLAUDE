#!/usr/bin/env python3
"""gui.py - Piccola interfaccia grafica (Tkinter, inclusa in Python) per cerca_preventivi."""

from __future__ import annotations

import os
import subprocess
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

sys.path.insert(0, str(Path(__file__).resolve().parent))

import cerca_preventivi as cp  # noqa: E402

QUI = Path(__file__).resolve().parent


def apri(percorso: Path):
    if sys.platform.startswith("win"):
        os.startfile(percorso)  # type: ignore[attr-defined]
    else:
        subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", str(percorso)])


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ricerca preventivi - Per. Agr. Angelo Chiminelli")
        self.geometry("900x560")
        self.cartella = tk.StringVar()
        self.config_path = tk.StringVar(value=str(QUI / "config.json") if (QUI / "config.json").exists() else "")
        self.uscita = tk.StringVar(value=str(Path.home() / "risultati_preventivi"))
        self.tutti, self.ocr, self.copia = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
        self.cache = tk.BooleanVar(value=True)
        self.risultati: list = []

        f = ttk.Frame(self, padding=10)
        f.pack(fill="both", expand=True)
        for riga, (etich, var, cmd) in enumerate((
                ("Cartella da analizzare", self.cartella, self._scegli_cartella),
                ("Configurazione (.json)", self.config_path, self._scegli_config),
                ("Cartella risultati", self.uscita, self._scegli_uscita))):
            ttk.Label(f, text=etich).grid(row=riga, column=0, sticky="w")
            ttk.Entry(f, textvariable=var, width=80).grid(row=riga, column=1, sticky="we", padx=5)
            ttk.Button(f, text="Sfoglia...", command=cmd).grid(row=riga, column=2)
        op = ttk.Frame(f)
        op.grid(row=3, column=0, columnspan=3, sticky="w", pady=6)
        ttk.Checkbutton(op, text="Analizza tutti i file (non solo nome 'preventivo/offerta')",
                        variable=self.tutti).pack(side="left")
        ttk.Checkbutton(op, text="OCR PDF scansionati", variable=self.ocr).pack(side="left", padx=8)
        ttk.Checkbutton(op, text="Scansione incrementale", variable=self.cache).pack(side="left")
        ttk.Checkbutton(op, text="Copia confermati/probabili", variable=self.copia).pack(side="left", padx=8)
        self.avvia = ttk.Button(f, text="AVVIA SCANSIONE", command=self._avvia)
        self.avvia.grid(row=4, column=0, columnspan=3, pady=4)
        self.stato = ttk.Label(f, text="")
        self.stato.grid(row=5, column=0, columnspan=3, sticky="w")

        colonne = ("esito", "punti", "file", "oggetto", "importo")
        self.tab = ttk.Treeview(f, columns=colonne, show="headings")
        for c, w in zip(colonne, (110, 50, 380, 230, 90)):
            self.tab.heading(c, text=c.capitalize())
            self.tab.column(c, width=w, stretch=c in ("file", "oggetto"))
        self.tab.grid(row=6, column=0, columnspan=3, sticky="nsew")
        self.tab.bind("<Double-1>", lambda e: self._apri_documento())
        b = ttk.Frame(f)
        b.grid(row=7, column=0, columnspan=3, pady=6)
        ttk.Button(b, text="Mostra evidenza", command=self._evidenza).pack(side="left")
        ttk.Button(b, text="Apri documento", command=self._apri_documento).pack(side="left", padx=5)
        ttk.Button(b, text="Apri cartella", command=lambda: self._apri_documento(cartella=True)).pack(side="left")
        ttk.Button(b, text="Apri report (Excel)", command=self._apri_report).pack(side="left", padx=5)
        f.columnconfigure(1, weight=1)
        f.rowconfigure(6, weight=1)

    def _scegli_cartella(self):
        self.cartella.set(filedialog.askdirectory() or self.cartella.get())

    def _scegli_config(self):
        self.config_path.set(filedialog.askopenfilename(filetypes=[("JSON", "*.json")]) or self.config_path.get())

    def _scegli_uscita(self):
        self.uscita.set(filedialog.askdirectory() or self.uscita.get())

    def _avvia(self):
        if not Path(self.cartella.get()).is_dir():
            messagebox.showerror("Errore", "Scegliere una cartella da analizzare.")
            return
        self.avvia.state(["disabled"])
        self.tab.delete(*self.tab.get_children())
        threading.Thread(target=self._lavora, daemon=True).start()

    def _lavora(self):
        uscita = Path(self.uscita.get())
        uscita.mkdir(parents=True, exist_ok=True)
        n = [0]

        def passo(r):
            n[0] += 1
            self.after(0, lambda: self.stato.config(text=f"{n[0]} documenti analizzati... {Path(r.file).name}"))
        try:
            cfg = cp.carica_config(self.config_path.get() or None)
            ris = cp.scansiona([Path(self.cartella.get())], cfg, self.tutti.get(), self.ocr.get(),
                               uscita / "indice.sqlite" if self.cache.get() else None, passo)
            cp.scrivi_report(ris, uscita / "report_preventivi.csv")
            if self.copia.get():
                cp.copia_risultati(ris, [Path(self.cartella.get())], uscita / "copie",
                                   {"CONFERMATO", "PROBABILE"})
            self.after(0, self._mostra, ris)
        except Exception as exc:
            msg = str(exc)
            self.after(0, lambda: messagebox.showerror("Errore", msg))
        finally:
            self.after(0, lambda: self.avvia.state(["!disabled"]))

    def _mostra(self, ris):
        self.risultati = ris
        for i, r in enumerate(ris):
            self.tab.insert("", "end", iid=str(i), values=(
                r.esito + (" (dup.)" if r.duplicato_di else ""), f"{r.punti_autore:g}",
                r.file, r.oggetto[:80], r.importo))
        self.stato.config(text="Fatto: " + (cp.riepilogo(ris) or "nessun documento trovato"))

    def _selezionato(self):
        sel = self.tab.selection()
        return self.risultati[int(sel[0])] if sel else None

    def _evidenza(self):
        r = self._selezionato()
        if r:
            messagebox.showinfo(r.esito, "\n".join([
                f"File: {r.file}", f"Esito: {r.esito}  (punti emittente {r.punti_autore:g}, "
                f"preventivo {r.punti_preventivo:g})", f"Emittente presunto: {r.emittente_presunto}",
                f"Firmatari p7m: {r.firmatari or '-'}", f"Oggetto: {r.oggetto}",
                f"Importo: {r.importo}   Data: {r.data}", "", "Motivi:",
                *[f"  - {m}" for m in r.motivi], "", f"Evidenza: {r.evidenza}"]))

    def _apri_documento(self, cartella=False):
        r = self._selezionato()
        if r:
            apri(Path(r.file).parent if cartella else Path(r.file))

    def _apri_report(self):
        p = Path(self.uscita.get()) / "report_preventivi.csv"
        if p.exists():
            apri(p)


if __name__ == "__main__":
    App().mainloop()
