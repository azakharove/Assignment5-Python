from backtester.broker import Broker

def test_broker(broker):
    assert broker.cash == 1_000
    assert broker.position == 0

    broker.market_order(side="BUY", qty=100, price=10.0)
