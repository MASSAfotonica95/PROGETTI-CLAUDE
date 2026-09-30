"""Conversioni di coordinate senza dipendenze esterne (UTM ETRS89/WGS84 -> lat/lon e ritorno)."""
from __future__ import annotations

import math

# GRS80/WGS84 (differenza trascurabile ai fini di questo uso: < 1 mm nella pratica)
_A = 6378137.0
_F = 1 / 298.257222101
_K0 = 0.9996
_E2 = _F * (2 - _F)
_EP2 = _E2 / (1 - _E2)


def _central_meridian(zone: int) -> float:
    return math.radians(zone * 6 - 183)


def latlon_to_utm(lat: float, lon: float, zone: int) -> tuple[float, float]:
    phi, lam = math.radians(lat), math.radians(lon)
    lam0 = _central_meridian(zone)
    n = _A / math.sqrt(1 - _E2 * math.sin(phi) ** 2)
    t = math.tan(phi) ** 2
    c = _EP2 * math.cos(phi) ** 2
    a = math.cos(phi) * (lam - lam0)
    e4, e6 = _E2 ** 2, _E2 ** 3
    m = _A * ((1 - _E2 / 4 - 3 * e4 / 64 - 5 * e6 / 256) * phi
              - (3 * _E2 / 8 + 3 * e4 / 32 + 45 * e6 / 1024) * math.sin(2 * phi)
              + (15 * e4 / 256 + 45 * e6 / 1024) * math.sin(4 * phi)
              - (35 * e6 / 3072) * math.sin(6 * phi))
    x = _K0 * n * (a + (1 - t + c) * a ** 3 / 6
                   + (5 - 18 * t + t ** 2 + 72 * c - 58 * _EP2) * a ** 5 / 120) + 500000.0
    y = _K0 * (m + n * math.tan(phi) * (a ** 2 / 2 + (5 - t + 9 * c + 4 * c ** 2) * a ** 4 / 24
                                        + (61 - 58 * t + t ** 2 + 600 * c - 330 * _EP2) * a ** 6 / 720))
    return x, y


def utm_to_latlon(easting: float, northing: float, zone: int, south: bool = False) -> tuple[float, float]:
    x = easting - 500000.0
    y = northing - (10000000.0 if south else 0.0)
    e1 = (1 - math.sqrt(1 - _E2)) / (1 + math.sqrt(1 - _E2))
    e4, e6 = _E2 ** 2, _E2 ** 3
    m = y / _K0
    mu = m / (_A * (1 - _E2 / 4 - 3 * e4 / 64 - 5 * e6 / 256))
    phi1 = (mu + (3 * e1 / 2 - 27 * e1 ** 3 / 32) * math.sin(2 * mu)
            + (21 * e1 ** 2 / 16 - 55 * e1 ** 4 / 32) * math.sin(4 * mu)
            + (151 * e1 ** 3 / 96) * math.sin(6 * mu)
            + (1097 * e1 ** 4 / 512) * math.sin(8 * mu))
    n1 = _A / math.sqrt(1 - _E2 * math.sin(phi1) ** 2)
    t1 = math.tan(phi1) ** 2
    c1 = _EP2 * math.cos(phi1) ** 2
    r1 = _A * (1 - _E2) / (1 - _E2 * math.sin(phi1) ** 2) ** 1.5
    d = x / (n1 * _K0)
    phi = phi1 - (n1 * math.tan(phi1) / r1) * (
        d ** 2 / 2 - (5 + 3 * t1 + 10 * c1 - 4 * c1 ** 2 - 9 * _EP2) * d ** 4 / 24
        + (61 + 90 * t1 + 298 * c1 + 45 * t1 ** 2 - 252 * _EP2 - 3 * c1 ** 2) * d ** 6 / 720)
    lam = _central_meridian(zone) + (
        d - (1 + 2 * t1 + c1) * d ** 3 / 6
        + (5 - 2 * c1 + 28 * t1 - 3 * c1 ** 2 + 8 * _EP2 + 24 * t1 ** 2) * d ** 5 / 120) / math.cos(phi1)
    return math.degrees(phi), math.degrees(lam)


def parse_coordinate(text: str) -> tuple[float, float]:
    """Accetta 'lat,lon' (gradi decimali WGS84, anche con spazi o ';')."""
    parts = text.replace(";", ",").replace(" ", ",").split(",")
    nums = [p for p in parts if p]
    if len(nums) != 2:
        raise ValueError("Formato atteso: 'lat,lon' in gradi decimali WGS84")
    return float(nums[0]), float(nums[1])


def bbox_contains(bbox: list[float], lat: float, lon: float) -> bool:
    """bbox = [lon_min, lat_min, lon_max, lat_max]."""
    return bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]
