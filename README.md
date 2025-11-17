# Assignment 5: Testing & CI in Financial Engineering

## Design Notes

The backtester consists of four core components:

- **PriceLoader**: Generates synthetic price data for testing (no external API calls)
- **VolatilityBreakoutStrategy**: Calculates rolling volatility and generates BUY/HOLD signals when daily return exceeds the rolling volatility threshold
- **Broker**: Manages cash and positions, executes market orders with validation (rejects invalid orders, insufficient cash/shares)
- **Backtester**: Orchestrates the backtesting loop - computes signals at t-1, executes trades at t, tracks equity

**Key Design Decisions:**
- Signals use t-1 data to trade at t (realistic lookback)
- Broker raises `ValueError` for invalid orders (testable failure paths)
- All components use type hints and enums (`Signal`, `Side`, `MarketOrder`) for clarity
- Tests use synthetic data fixtures to ensure determinism and speed

## Running Tests

```bash
pip install -r requirements.txt
pytest
```

## Coverage Report

HTML coverage report available in `htmlcov/index.html`. Open it in a browser to view detailed coverage metrics.

```bash
coverage run -m pytest
coverage html
```

## CI Status

✅ **CI Pipeline**: [Successful CI Job](https://github.com/azakharove/Assignment5-Python/actions/runs/19394449899/job/55492480160)

Tests run on every push/PR with coverage enforcement (≥90% required).
