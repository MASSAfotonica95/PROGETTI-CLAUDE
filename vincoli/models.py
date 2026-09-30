from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any


class Status(str, Enum):
    HIT = "INTERCETTATO"            # il servizio ha risposto: il punto ricade nell'elemento
    NEARBY = "ENTRO_RAGGIO"         # non sul punto, ma entro il raggio richiesto
    NO_HIT = "NESSUN_ELEMENTO"      # il servizio ha risposto: nessun elemento su quel livello
    UNVERIFIED = "NON_VERIFICATO"   # servizio non raggiungibile / risposta non valida
    NOT_APPLICABLE = "NON_APPLICABILE"  # fuori dall'area di copertura della fonte
    MANUAL = "VERIFICA_MANUALE"     # nessuna API: fonte documentale da consultare


@dataclass
class Point:
    lat: float
    lon: float

    def __post_init__(self):
        if not (-90 <= self.lat <= 90 and -180 <= self.lon <= 180):
            raise ValueError(f"Coordinate fuori range: lat={self.lat}, lon={self.lon}")


@dataclass
class Finding:
    source_id: str
    source_name: str
    layer: str
    theme: str
    status: Status
    legal_ref: str = ""
    attributes: list[dict[str, Any]] = field(default_factory=list)
    summary: list[str] = field(default_factory=list)   # righe leggibili per gli attributi chiave
    links: list[str] = field(default_factory=list)     # documenti/atti collegati
    query_url: str = ""
    detail: str = ""       # errore o nota
    queried_at: str = ""
    provider: str = ""
    value_note: str = ""   # valore giuridico del dato

    def to_dict(self):
        d = asdict(self)
        d["status"] = self.status.value
        return d
