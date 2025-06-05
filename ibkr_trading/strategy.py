"""Simple strategy implementations."""

import pandas as pd


def sma_signal(df: pd.DataFrame, short: int = 10, long: int = 30) -> str:
    """Simple moving average crossover signal."""
    df = df.copy()
    df['ma_s'] = df['close'].rolling(short).mean()
    df['ma_l'] = df['close'].rolling(long).mean()

    if len(df) < max(short, long) + 1:
        return 'HOLD'

    if df['ma_s'].iloc[-2] < df['ma_l'].iloc[-2] and df['ma_s'].iloc[-1] > df['ma_l'].iloc[-1]:
        return 'BUY'
    elif df['ma_s'].iloc[-2] > df['ma_l'].iloc[-2] and df['ma_s'].iloc[-1] < df['ma_l'].iloc[-1]:
        return 'SELL'
    return 'HOLD'
