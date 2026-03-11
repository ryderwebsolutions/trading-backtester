import pandas as pd
from backtester import BacktestEngine
from strategies.moving_average import MovingAverageCrossover

def test_backtest_runs():
    data = pd.read_csv('data/sample.csv', parse_dates=True, index_col=0)
    strat = MovingAverageCrossover(short_window=2, long_window=3)
    engine = BacktestEngine(data, strat)
    results = engine.run()
    assert 'strategy_returns' in results.columns
    summary = engine.summary()
    assert 'sharpe_ratio' in summary
    assert 'max_drawdown' in summary
    assert 'total_return' in summary
