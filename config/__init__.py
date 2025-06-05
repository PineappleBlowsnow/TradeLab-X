"""Project configuration package."""

from .trading import (
    HOST,
    PORT,
    CLIENT_ID,
    DEFAULT_SYMBOL,
    HIST_DURATION,
    BAR_SIZE,
)

__all__ = [
    "HOST",
    "PORT",
    "CLIENT_ID",
    "DEFAULT_SYMBOL",
    "HIST_DURATION",
    "BAR_SIZE",
]
