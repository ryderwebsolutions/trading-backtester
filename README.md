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

Data must be a CSV with a datetime index in the first column and at least a
`Close` price column. Put example files under `data/` as shown.

### Running the backtester

Install dependencies:

```bash
pip install -r requirements.txt
```

Then invoke the CLI script:

```bash
python main.py data/your_history.csv --strategy ma --short 20 --long 50
```

You can switch strategies (`ma`, `meanrev`, `rsi`) and tune parameters via
command‑line options. Transaction costs and slippage can be specified with
`--cost` and `--slippage`.

Example output:

```
$ python main.py data/sample.csv --strategy rsi --period 3 --lower 25 --upper 75
Performance:
  sharpe_ratio: 0.1234
  max_drawdown: -0.0456
  total_return: 0.0789
```

### Strategies

- **ma**: moving average crossover
- **meanrev**: z‑score mean reversion
- **rsi**: RSI overbought/oversold

Add your own by dropping a class in `trading_backtester/strategies` with a
`generate_signals(df)` method that returns a DataFrame containing a `signal`
column.


## Writing Strategies

Create a new class in the `strategies/` folder with a `generate_signals(data)` method that returns a DataFrame with a `signal` column (1 for long, -1 for short, 0 for neutral).

## Metrics

- Sharpe ratio
- Max drawdown
- Total return

## Testing

The project includes basic tests powered by `pytest`. After installing requirements, run:

```bash
pytest
```

