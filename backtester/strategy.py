import statistics
import pandas as pd
import numpy as np

from typing import Dict, List

class VolatilityBreakoutStrategy:
    """
    Buy if daily return > rolling volatility over window of specified number of days
    """
    def __init__(self, window = 20, quantity: int = 100):
        self.quantity = quantity
        self.window = window
        self.volatility_history: Dict[str, List[float]] = {}

    def _calculate_volatility(self, prices: pd.Series) -> float:
        if len(prices) < self.window:
            return 0.0

        returns = (prices / prices.shift(1) - 1).dropna()
        return returns.rolling(window=self.window).std().iloc[-1]

    def signals(self, prices: pd.Series) -> pd.Series:
        signals = pd.Series(dtype=object)
        prev_prices = pd.Series(dtype=float)
        for index, price in prices.items():
            if len(prev_prices) < self.window + 1:
                prev_prices[index] = price
                signals.at[index] = "HOLD"
                # print(index, ": ", price, "HOLD")
                continue

            rolling_vol = self._calculate_volatility(prev_prices)
            current_return = (price / prev_prices.iloc[-1]) - 1

            if current_return > rolling_vol:
                signals.at[index] = (self.quantity, price, "BUY")

            prev_prices.at[index] = price
            # print(index, ": ", price, "vol: ", rolling_vol, " return: ", current_return)

        return signals
