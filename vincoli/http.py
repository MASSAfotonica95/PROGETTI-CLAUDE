"""Client HTTP condiviso: retry, timeout, User-Agent identificabile, rispetto del proxy d'ambiente."""
from __future__ import annotations

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

USER_AGENT = "vincoli-territoriali/0.1 (verifica vincoli su coordinata; uso tecnico)"
DEFAULT_TIMEOUT = 30


def make_session(retries: int = 2) -> requests.Session:
    s = requests.Session()
    retry = Retry(total=retries, backoff_factor=1, status_forcelist=(502, 503, 504),
                  allowed_methods=("GET", "POST"), raise_on_status=False)
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    s.headers["User-Agent"] = USER_AGENT
    return s
