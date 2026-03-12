import argparse
import pandas as pd

from . import BacktestEngine
from .strategies.moving_average import MovingAverageCrossover
from .strategies.mean_reversion import MeanReversion


def load_data(csv_path):
    df = pd.read_csv(csv_path, parse_dates=True, index_col=0)
    return df


def select_strategy(name: str, **kwargs):
    name = name.lower()
    if name == 'ma':
        return MovingAverageCrossover(**kwargs)
    if name == 'meanrev':
        return MeanReversion(**kwargs)
    if name == 'rsi':
        from .strategies.rsi import RSIStrategy

        return RSIStrategy(**kwargs)
    raise ValueError(f"Unknown strategy '{name}'")


def main():
    parser = argparse.ArgumentParser(description='Run a backtest from CSV data')
    parser.add_argument('csv', help='path to price CSV file')
    parser.add_argument('--strategy', '-s', default='ma', help='strategy name (ma, meanrev)')
    parser.add_argument('--short', type=int, default=20, help='short window for MA')
    parser.add_argument('--long', type=int, default=50, help='long window for MA')
    parser.add_argument('--window', type=int, default=20, help='window for mean-reversion')
    parser.add_argument('--threshold', type=float, default=1.5, help='z-score threshold for mean-reversion')
    parser.add_argument('--period', type=int, default=14, help='RSI lookback period')
    parser.add_argument('--lower', type=float, default=30, help='RSI lower threshold')
    parser.add_argument('--upper', type=float, default=70, help='RSI upper threshold')
    parser.add_argument('--cost', type=float, default=0.0, help='transaction cost fraction')
    parser.add_argument('--slippage', type=float, default=0.0, help='slippage fraction')

    args = parser.parse_args()

    data = load_data(args.csv)
    strat_kwargs = {}
    if args.strategy == 'ma':
        strat_kwargs = {'short_window': args.short, 'long_window': args.long}
    elif args.strategy == 'meanrev':
        strat_kwargs = {'window': args.window, 'threshold': args.threshold}
    elif args.strategy == 'rsi':
        strat_kwargs = {'period': args.period, 'lower': args.lower, 'upper': args.upper}

    strategy = select_strategy(args.strategy, **strat_kwargs)
    engine = BacktestEngine(data, strategy, transaction_cost=args.cost, slippage=args.slippage)
    results = engine.run()
    print('Performance:')
    for k, v in engine.summary().items():
        print(f"  {k}: {v:.4f}")


if __name__ == '__main__':
    main()
