"""Entry point for trading system."""

from .ib_connector import IBConnector
from .signal import generate_signal
from .execution import execute_trade
from config import trading as config


def run():
    """Run a simple trading loop for demonstration."""
    ib_api = IBConnector()
    contract = ib_api.get_stock_contract(config.DEFAULT_SYMBOL)
    df = ib_api.get_historical_data(contract)

    if df.empty:
        print("No data returned")
        return

    df['close'] = df['close'].astype(float)
    signal = generate_signal(df)
    print(f"Signal: {signal}")

    if signal in {'BUY', 'SELL'}:
        execute_trade(ib_api.ib, contract, signal, 100)


if __name__ == '__main__':
    run()
