"""Versione web: genera un unico HTML autonomo e, opzionalmente, lo serve in locale con un
proxy ristretto (lista host consentiti) per le fonti che bloccano le richieste dal browser (es. ISPRA).

    python -m vincoli.webapp                 # server su http://127.0.0.1:8765
    python -m vincoli.webapp --export out.html   # file HTML statico (senza proxy)
"""
from __future__ import annotations

import argparse
import json
import sys
import threading
import urllib.error
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import USER_AGENT
from .registry import load_sources

TEMPLATE = Path(__file__).parent / "web" / "template.html"


def render_html(extra_dirs: list[str] | None = None) -> str:
    reg = json.dumps({"sources": load_sources(extra_dirs)}, ensure_ascii=False).replace("</", "<\\/")
    return TEMPLATE.read_text(encoding="utf-8").replace("/*REGISTRY*/null", reg)


def allowed_hosts(extra_dirs: list[str] | None = None) -> set[str]:
    return {urlparse(s["url"]).hostname for s in load_sources(extra_dirs) if s.get("browser_proxy")}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def make_handler(html: str, hosts: set[str], port: int):
    opener = urllib.request.build_opener(_NoRedirect)
    own = {f"127.0.0.1:{port}", f"localhost:{port}"}

    class H(BaseHTTPRequestHandler):
        server_version = "vincoli"

        def log_message(self, *a):
            pass

        def _send(self, code, body: bytes, ctype="text/plain; charset=utf-8"):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            # anti DNS-rebinding / uso da altri siti: solo Host locale e, se presente, Origin proprio
            origin = self.headers.get("Origin")
            if self.headers.get("Host") not in own or (origin and urlparse(origin).netloc not in own):
                return self._send(403, b"forbidden")
            u = urlparse(self.path)
            if u.path == "/":
                return self._send(200, html.encode("utf-8"), "text/html; charset=utf-8")
            if u.path == "/__proxy_ok":
                return self._send(200, b"ok")
            if u.path == "/proxy":
                target = (parse_qs(u.query).get("url") or [""])[0]
                t = urlparse(target)
                if t.scheme != "https" or t.hostname not in hosts or t.port not in (None, 443):
                    return self._send(403, b"host non consentito")
                req = urllib.request.Request(target, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
                try:
                    with opener.open(req, timeout=40) as r:
                        return self._send(200, r.read(), r.headers.get("Content-Type", "application/json"))
                except urllib.error.HTTPError as e:
                    return self._send(e.code, f"upstream HTTP {e.code}".encode())
                except Exception as e:  # noqa: BLE001
                    return self._send(502, f"upstream error: {type(e).__name__}".encode())
            self._send(404, b"not found")

    return H


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="vincoli.webapp")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--export", metavar="FILE", help="scrive l'HTML statico e termina")
    ap.add_argument("--sources-dir", action="append")
    ap.add_argument("--no-browser", action="store_true")
    a = ap.parse_args(argv)
    html = render_html(a.sources_dir)
    if a.export:
        Path(a.export).write_text(html, encoding="utf-8")
        print(f"scritto {a.export} ({len(html) // 1024} KB)")
        return 0
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), make_handler(html, allowed_hosts(a.sources_dir), a.port))
    url = f"http://127.0.0.1:{a.port}/"
    print(f"Vincoli su coordinata: {url}  (Ctrl+C per uscire)")
    if not a.no_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
