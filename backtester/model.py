from dataclasses import dataclass
from enum import Enum

class Signal(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

class Side(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

@dataclass
class MarketOrder:
    side: Side
    qty: int
    price: float

def to_side(signal: Signal) -> Side:
    match signal:
        case Signal.BUY:
            return Side.BUY
        case Signal.SELL:
            return Side.SELL
        case Signal.HOLD:
            raise ValueError("HOLD is not a valid side")