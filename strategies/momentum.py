"""Momentum-based strategy examples."""

from __future__ import annotations

import pandas as pd


def sma_crossover(df: pd.DataFrame, fast: int = 10, slow: int = 30) -> str:
    """Return BUY/SELL/HOLD signal using a simple moving average crossover."""
    if len(df) < max(fast, slow) + 1:
        return 'HOLD'

    ma_fast = df['close'].rolling(fast).mean()
    ma_slow = df['close'].rolling(slow).mean()

    if ma_fast.iloc[-2] < ma_slow.iloc[-2] and ma_fast.iloc[-1] > ma_slow.iloc[-1]:
        return 'BUY'
    if ma_fast.iloc[-2] > ma_slow.iloc[-2] and ma_fast.iloc[-1] < ma_slow.iloc[-1]:
        return 'SELL'
    return 'HOLD'
