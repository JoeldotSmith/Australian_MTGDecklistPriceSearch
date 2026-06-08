from dataclasses import dataclass
from typing import Optional


@dataclass
class CardResult:
    card_name: str
    set_name: str
    condition: str
    qty: int
    price_cents: int
    url: Optional[str] = None
