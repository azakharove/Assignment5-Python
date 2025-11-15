import pytest
from backtester.broker import Broker
from backtester.model import MarketOrder, Side

def test_broker(broker):
    assert broker.cash == 1_000
    assert broker.position == 0

    order = MarketOrder(Side.BUY, qty=100, price=10.0)
    broker.market_order(order)
    assert broker.position == 100
    assert broker.cash == 1_000 - (100 * 10.0)

def test_rejects_bad_orders(broker):
    
    # try to buy more than the broker has cash
    with pytest.raises(ValueError):
        broker.market_order(MarketOrder(Side.BUY, qty=100, price=1000.0))
    
    # try to sell more than the broker has position
    with pytest.raises(ValueError):
        broker.market_order(MarketOrder(Side.SELL, qty=100, price=10.0))
    
    # rejects qty=0
    with pytest.raises(ValueError):
        broker.market_order(MarketOrder(Side.BUY, qty=0, price=10.0))
    
