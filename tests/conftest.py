import pytest
from backtester.strategy import VolatilityBreakoutStrategy
from backtester.broker import Broker
from backtester.price_loader import PriceLoader

@pytest.fixture
def prices():
    loader = PriceLoader(start_price=100.0, seed=42)
    return loader.load("AAPL", num_days=200)

@pytest.fixture
def strategy():
    return VolatilityBreakoutStrategy()

@pytest.fixture
def broker():
    return Broker(cash=1_000)