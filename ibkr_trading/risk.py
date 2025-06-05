"""Basic risk management utilities."""


def determine_position_size(account_value: float, risk_per_trade: float = 0.01, stop_loss_pct: float = 0.02) -> float:
    """Compute position size based on account value and risk parameters."""
    risk_amount = account_value * risk_per_trade
    return risk_amount / stop_loss_pct
