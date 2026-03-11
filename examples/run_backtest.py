"""Example script showing how to import and use the package."""
import pandas as pd
from trading_backtester import BacktestEngine
from trading_backtester.strategies.moving_average import MovingAverageCrossover


def main():
    data = pd.read_csv('data/sample.csv', parse_dates=True, index_col=0)
    strat = MovingAverageCrossover(short_window=5, long_window=10)
    engine = BacktestEngine(data, strat, transaction_cost=0.001)
    results = engine.run()
    print('Summary:', engine.summary())


if __name__ == '__main__':
    main()
