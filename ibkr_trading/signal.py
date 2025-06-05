"""Signal generation utilities."""

from .strategy import sma_signal


def generate_signal(df):
    """Return a signal string for the given dataframe."""
    return sma_signal(df)
