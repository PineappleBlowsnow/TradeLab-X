"""Live trading session utilities."""

from __future__ import annotations

from ibkr_trading.ib_connector import IBConnector
from ibkr_trading.execution import execute_trade


class LiveTradingSession:
    """Simple wrapper to place trades via IBKR."""

    def __init__(self, symbol: str):
        self.ib_api = IBConnector()
        self.contract = self.ib_api.get_stock_contract(symbol)

    def place_order(self, action: str, quantity: int):
        execute_trade(self.ib_api.ib, self.contract, action, quantity)
