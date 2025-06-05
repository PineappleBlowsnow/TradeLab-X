"""IBKR connection and data utilities using ib_insync."""

from ib_insync import IB, Stock, util
import pandas as pd

from config import trading as config


class IBConnector:
    """Wrapper around ib_insync.IB for connection and basic data methods."""

    def __init__(self, host: str = config.HOST, port: int = config.PORT, client_id: int = config.CLIENT_ID):
        self.ib = IB()
        self.ib.connect(host, port, client_id)

    def get_stock_contract(self, symbol: str, exchange: str = 'SMART', currency: str = 'USD'):
        """Return an IBKR Stock contract."""
        return Stock(symbol, exchange, currency)

    def get_historical_data(self, contract, duration: str = config.HIST_DURATION, bar_size: str = config.BAR_SIZE):
        """Request historical bar data and return as pandas DataFrame."""
        bars = self.ib.reqHistoricalData(
            contract,
            endDateTime='',
            durationStr=duration,
            barSizeSetting=bar_size,
            whatToShow='TRADES',
            useRTH=True,
            formatDate=1,
        )
        df = util.df(bars)
        return df

    def place_order(self, contract, order):
        trade = self.ib.placeOrder(contract, order)
        return trade
