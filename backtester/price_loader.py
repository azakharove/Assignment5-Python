import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class PriceLoader:
    
    def __init__(self, start_price: float = 100.0, seed: int = None):
        self.start_price = start_price
        self.seed = seed
        if seed is not None:
            np.random.seed(seed)
    
    def load(self, symbol: str, num_days: int = 200) -> pd.Series:

        dates = pd.date_range(
            start=datetime(2020, 1, 1),
            periods=num_days,
            freq='D'
        )
        
        # Simple random walk for prices
        if self.seed is not None:
            np.random.seed(self.seed)
        
        returns = np.random.normal(0.001, 0.02, num_days)
        prices = self.start_price * (1 + returns).cumprod()
        
        return pd.Series(prices, index=dates, name=symbol)
