"""Volume spike detection utilities."""

from __future__ import annotations

import pandas as pd

def volume_spike(df: pd.DataFrame, window: int = 20, threshold: float = 2.0) -> pd.Series:
    """Return a boolean Series where volume exceeds a threshold times the rolling mean."""
    avg_vol = df["volume"].rolling(window).mean()
    return df["volume"] > threshold * avg_vol
