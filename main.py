import pandas as pd
from backtester import BacktestEngine
from strategies.moving_average import MovingAverageCrossover
from strategies.mean_reversion import MeanReversion


def load_data(csv_path):
    df = pd.read_csv(csv_path, parse_dates=True, index_col=0)
    return df


def run_example():
    data = load_data('data/sample.csv')
    strategy = MovingAverageCrossover(20, 50)
    engine = BacktestEngine(data, strategy)
    results = engine.run()
    print(engine.summary())


if __name__ == '__main__':
    run_example()
