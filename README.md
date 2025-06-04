# TradeLab-X

**TradeLab-X** is a modular trading research and execution framework focused on engineering-driven analysis of price action and volume behavior. 
It bridges academic technical analysis with real-time automated execution via IBKR.

## Project Goals
- Integrate Python modules for data ingestion, strategy orchestration, and ML workflows
- Engineer a signal-processing pipeline for price & volume microstructure
- Support both research (backtest) and live deployment (IBKR)
- Enable multi-strategy stacking: trend, mean-reversion, breakout, etc.

## Modules Overview
- `core/`: Signal generation from price patterns, volume profile, order flow
    - `volume_spike.py`: Detect abnormal volume activity
    - `support_resistance.py`: Identify key support/resistance levels
- `strategies/`: Strategy logic, position sizing, and trade signals
- `backtest/`: Strategy evaluation and historical testing
- `live/`: IBKR API connection, real-time data, order execution
- `data/`: Data ingestion from IB, Yahoo Finance, or custom feeds

## Setup
```bash
pip install -r requirements.txt
```

## Roadmap
- [x] Core signal detectors (volume spike, support/resistance)
- [ ] SMA/EMA crossover strategy module
- [ ] IBKR live module using ib_insync
- [ ] Modular risk engine
- [ ] Research notebooks (alpha lab)

## License
GNU Affero General Public License v3.0 (AGPL-3.0)

## Language Architecture
- 🐍 **Full prototype**: Implemented in Python 3.10+
- 🤖 **Machine Learning modules**: Python + scikit-learn / XGBoost / PyTorch
- 🔌 **Live trading interface**: ib_insync + IBKR API

*Note: C++ integration remains an optional upgrade path if performance becomes a constraint.*
