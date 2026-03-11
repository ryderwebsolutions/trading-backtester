# Trading Backtester

A simple Python backtesting engine that loads historical price data from CSV files and evaluates trading strategies such as moving average crossover and mean reversion.

## Structure

```
trading-backtester
│
├── data/
├── strategies/
├── backtester.py
├── metrics.py
├── main.py
├── requirements.txt
└── README.md
```

## Usage

1. Place historical CSV files in the `data/` directory. The CSV must have a datetime index and at least a `Close` column.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run `python main.py` to execute an example backtest.

## Writing Strategies

Create a new class in the `strategies/` folder with a `generate_signals(data)` method that returns a DataFrame with a `signal` column (1 for long, -1 for short, 0 for neutral).

## Metrics

- Sharpe ratio
- Max drawdown
- Total return
