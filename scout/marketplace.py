from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Marketplace:
    code: str
    name: str
    currency: str
    referral_rate: float


MARKETPLACES = {
    "US": Marketplace("US", "Amazon.com", "USD", 0.15),
    "UK": Marketplace("UK", "Amazon.co.uk", "GBP", 0.15),
    "CA": Marketplace("CA", "Amazon.ca", "CAD", 0.15),
    "AE": Marketplace("AE", "Amazon.ae", "AED", 0.15),
}


def get_marketplace(code: str) -> Marketplace:
    return MARKETPLACES.get(code.upper(), MARKETPLACES["US"])
