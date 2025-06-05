"""Data ingestion helpers."""

from __future__ import annotations

import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load historical data from a CSV file."""
    return pd.read_csv(path)
