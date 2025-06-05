"""Order execution helpers."""

from ib_insync import MarketOrder


def execute_trade(ib, contract, action: str, quantity: int):
    """Submit a market order via ib_insync."""
    order = MarketOrder(action, quantity)
    trade = ib.placeOrder(contract, order)
    ib.sleep(1)
    return trade
