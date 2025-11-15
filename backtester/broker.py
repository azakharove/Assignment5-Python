from backtester.model import MarketOrder, Side

class Broker:
    def __init__(self, cash: float = 1_000_000):
        self.cash = cash
        self.position = 0

    def market_order(self, order: MarketOrder):
        
        if order.qty <= 0:
            raise ValueError("Quantity must be greater than 0")
            
        match order.side:
            case Side.BUY:
                if self.cash < order.qty * order.price:
                    raise ValueError("Insufficient cash to buy")
                self.cash -= order.qty * order.price
                self.position += order.qty
                print(f"Bought {order.qty} shares at {order.price}")
            case Side.SELL:
                if self.position < order.qty:
                    raise ValueError("Insufficient position to sell")
                self.cash += order.qty * order.price
                self.position -= order.qty
                print(f"Sold {order.qty} shares at {order.price}")