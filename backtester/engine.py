import pandas as pd

from backtester.model import MarketOrder, Signal, to_side

class Backtester:
    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run(self, prices: pd.Series):
        
        signals: pd.Series[Signal] = self.strategy.signals(prices)
        for i, (index, signal) in enumerate(signals.items()):
            if signal == Signal.HOLD:
                continue

            if i + 1 < len(prices):
                trade_price = prices.iloc[i + 1]
                try: 
                    self.broker.market_order(MarketOrder(to_side(signal), self.strategy.quantity, trade_price))
                except ValueError as e:
                    print(f"Failed to execute market order: {e}")
                    continue
        
        return self.broker.cash + self.broker.position * prices.iloc[-1]