import pandas as pd
from unittest.mock import MagicMock
from backtester.model import Signal
from backtester.engine import Backtester

def test_engine(prices, broker):
    fake_strategy = MagicMock()
    fake_signals = pd.Series([Signal.HOLD] * len(prices), index=prices.index)
    fake_signals.iloc[9] = Signal.BUY  # triggers buy at t=10
    fake_strategy.signals.return_value = fake_signals
    fake_strategy.quantity = 1 

    bt = Backtester(fake_strategy, broker)
    result = bt.run(prices)
    print(result)

    assert broker.position == 1
    assert broker.cash == 1000 - float(prices.iloc[10])
    assert result == broker.cash + broker.position * prices.iloc[-1]