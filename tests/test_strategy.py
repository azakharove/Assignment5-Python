import pandas as pd

from backtester.strategy import VolatilityBreakoutStrategy
from backtester.model import Signal

def test_signals_length(strategy, prices):
    signals = strategy.signals(prices)
    assert len(signals) == len(prices)

def test_empty_signals(strategy):
    prices = pd.Series([])
    signals = strategy.signals(prices)
    assert len(signals) == 0

def test_identical_prices():
    strategy = VolatilityBreakoutStrategy(window=5, quantity=100)
    prices = pd.Series([100] * 6)
    signals = strategy.signals(prices)
    assert all(signal == Signal.HOLD for signal in signals)

def test_buy_signal():
    strategy = VolatilityBreakoutStrategy(window=5, quantity=100)
    prices = pd.Series([100, 100.1, 100.2, 100.3, 100.4, 100.5, 101.5])
    signals = strategy.signals(prices)
    print(signals)
    assert all(signal == Signal.HOLD for signal in signals[:-1])
    assert signals.iloc[-1] == Signal.BUY

def test_calc_vol_zero_not_enough_prices(strategy):
    prices = pd.Series([100, 101, 102, 103, 104, 105])
    vol = strategy._calculate_volatility(prices)
    assert vol == 0.0

def test_calc_vol():
    strategy = VolatilityBreakoutStrategy(window=3, quantity=100)
    prices = pd.Series([100, 102, 101, 105])
    # Manually calculate expected volatility
    # [100, 102, 101, 105]
    # [NaN, 100, 102, 101]
    expected_vol = pd.Series([(102 / 100) - 1, (101 / 102) - 1, (105 / 101) - 1]).std()
    actual_vol = strategy._calculate_volatility(prices)
    assert actual_vol == expected_vol