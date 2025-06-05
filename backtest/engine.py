"""Simple backtesting engine skeleton."""

from __future__ import annotations

import pandas as pd
from typing import Callable, List


class BacktestEngine:
    """Iterates through data and records signals."""

    def __init__(self, data: pd.DataFrame, strategy: Callable[[pd.DataFrame], str]):
        self.data = data
        self.strategy = strategy

    def run(self) -> List[str]:
        """Run the strategy across the dataset and collect signals."""
        signals: List[str] = []
        for i in range(len(self.data)):
            subset = self.data.iloc[: i + 1]
            signals.append(self.strategy(subset))
        return signals
