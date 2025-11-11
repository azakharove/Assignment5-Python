from backtester.strategy import VolatilityBreakoutStrategy

def test_strategy(strategy, prices):
    assert strategy is not None
    signals = strategy.signals(prices) 
    assert signals is None