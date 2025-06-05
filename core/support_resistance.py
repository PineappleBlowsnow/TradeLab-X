"""Support and resistance utilities."""

from __future__ import annotations

import pandas as pd


def support_resistance_levels(df: pd.DataFrame, lookback: int = 20):
    """Return support and resistance levels using rolling extremes."""
    support = df['low'].rolling(lookback).min()
    resistance = df['high'].rolling(lookback).max()
    return support, resistance
