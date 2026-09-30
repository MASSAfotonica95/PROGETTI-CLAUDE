import unittest
from unittest import mock

from vincoli import connectors, geo
from vincoli.models import Point, Status
from vincoli.registry import applies, load_sources
from vincoli import engine


class FakeResp:
    def __init__(self, payload, ctype="application/json"):
        self._p, self.headers, self.text = payload, {"content-type": ctype}, str(payload)

    def raise_for_status(self): pass
    def json(self): return self._p


class FakeSession:
    def __init__(self, payload=None, exc=None):
        self.payload, self.exc, self.calls = payload, exc, []

    def get(self, url, params=None, timeout=None):
        self.calls.append((url, params))
        if self.exc:
            raise self.exc
        return FakeResp(self.payload)


SRC = {"id": "s", "name": "S", "url": "https://x/MapServer", "provider": "P"}
LAYER = {"id": 3, "name": "L", "theme": "t", "display_fields": ["A"]}


class Geo(unittest.TestCase):
    def test_utm_matches_reference(self):  # valori forniti dall'utente per il punto di Brescia
        e, n = geo.latlon_to_utm(45.546677946, 10.227873543, 32)
        self.assertAlmostEqual(e, 595850.405, delta=0.01)
        self.assertAlmostEqual(n, 5044415.501, delta=0.01)

    def test_roundtrip(self):
        lat, lon = geo.utm_to_latlon(595850.405, 5044415.501, 32)
        self.assertAlmostEqual(lat, 45.546677946, places=7)
        self.assertAlmostEqual(lon, 10.227873543, places=7)

    def test_parse_and_range(self):
        self.assertEqual(geo.parse_coordinate("45.5, 10.2"), (45.5, 10.2))
        with self.assertRaises(ValueError):
            Point(120, 10)


class Connectors(unittest.TestCase):
    def test_arcgis_hit(self):
        s = FakeSession({"features": [{"attributes": {"A": "x"}}]})
        f = connectors.query_arcgis(s, SRC, LAYER, Point(45, 10))
        self.assertEqual(f.status, Status.HIT)
        self.assertEqual(f.summary, ["A=x"])
        self.assertEqual(s.calls[0][1]["geometry"], "10,45")  # lon,lat

    def test_arcgis_empty_is_no_hit(self):
        f = connectors.query_arcgis(FakeSession({"features": []}), SRC, LAYER, Point(45, 10))
        self.assertEqual(f.status, Status.NO_HIT)

    def test_errors_never_become_no_hit(self):
        import requests
        f = connectors.query_arcgis(FakeSession(exc=requests.ConnectionError("down")), SRC, LAYER, Point(45, 10))
        self.assertEqual(f.status, Status.UNVERIFIED)
        f = connectors.query_arcgis(FakeSession({"error": {"code": 400}}), SRC, LAYER, Point(45, 10))
        self.assertEqual(f.status, Status.UNVERIFIED)

    def test_wfs_uses_explicit_srid(self):
        s = FakeSession({"features": []})
        connectors.query_wfs(s, {**SRC, "url": "https://x/wfs"}, {**LAYER, "typename": "a:b"}, Point(44.4, 8.9))
        self.assertIn("SRID=4326;POINT(8.9 44.4)", s.calls[0][1]["CQL_FILTER"])


class Registry(unittest.TestCase):
    def test_default_sources_valid(self):
        for s in load_sources():
            self.assertIn(s["type"], ("arcgis", "wfs", "wms", "manual"))

    def test_applicability(self):
        brescia = next(s for s in load_sources() if s["id"] == "doc_brescia")
        self.assertTrue(applies(brescia, 45.5, 10.2, {"comune": "Brescia"}))
        self.assertFalse(applies(brescia, 45.5, 10.2, {"comune": "Milano"}))
        lomb = next(s for s in load_sources() if s["id"] == "lombardia_siba_paesaggio")
        self.assertFalse(applies(lomb, 41.9, 12.5, {}))  # Roma: fuori Lombardia


class Engine(unittest.TestCase):
    def test_run_with_fake_services(self):
        fake = FakeSession({"features": [{"attributes": {"DESC_DECR2": "Zona X"}}]})
        with mock.patch.object(engine, "make_session", return_value=fake), \
             mock.patch.object(engine, "reverse_geocode", return_value={"ok": True, "comune": "Brescia"}):
            res = engine.run(Point(45.5467, 10.2279), only=["lombardia_siba_paesaggio", "doc_brescia"])
        st = {f.status for f in res["findings"]}
        self.assertIn(Status.HIT, st)
        self.assertIn(Status.MANUAL, st)

    def test_outage_reported_not_hidden(self):
        import requests
        fake = FakeSession(exc=requests.ConnectionError("x"))
        with mock.patch.object(engine, "make_session", return_value=fake):
            res = engine.run(Point(45.5467, 10.2279), only=["eea_cdda"], geocode=False)
        self.assertTrue(all(f.status == Status.UNVERIFIED for f in res["findings"]))


if __name__ == "__main__":
    unittest.main()


class Web(unittest.TestCase):
    def test_html_embeds_registry_and_is_stdlib_only(self):
        import subprocess, sys
        code = "import sys; sys.modules['requests']=None; from vincoli import webapp; h=webapp.render_html(); print('lombardia_siba_paesaggio' in h, '/*REGISTRY*/' in h)"
        out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
        self.assertEqual(out.stdout.split(), ["True", "False"], out.stderr)

    def test_proxy_allowlist_and_host_checks(self):
        import threading, urllib.request, urllib.error
        from http.server import ThreadingHTTPServer
        from vincoli import webapp
        srv = ThreadingHTTPServer(("127.0.0.1", 0), None)
        port = srv.server_address[1]
        srv.RequestHandlerClass = webapp.make_handler("<html>", {"sdi.isprambiente.it"}, port)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

        def code(path, headers=None):
            try:
                return opener.open(urllib.request.Request(f"http://127.0.0.1:{port}{path}", headers=headers or {})).status
            except urllib.error.HTTPError as e:
                return e.code
        try:
            self.assertEqual(code("/__proxy_ok"), 200)
            self.assertEqual(code("/proxy?url=https://example.com/"), 403)                 # host non in lista
            self.assertEqual(code("/proxy?url=http://sdi.isprambiente.it/x"), 403)         # solo https
            self.assertEqual(code("/__proxy_ok", {"Host": "evil.test"}), 403)              # DNS rebinding
            self.assertEqual(code("/__proxy_ok", {"Origin": "https://evil.test"}), 403)    # altro sito
        finally:
            srv.shutdown()
