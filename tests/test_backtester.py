import pandas as pd
from trading_backtester import BacktestEngine
from trading_backtester.strategies.moving_average import MovingAverageCrossover

def test_backtest_runs():
    data = pd.read_csv('data/sample.csv', parse_dates=True, index_col=0)
    strat = MovingAverageCrossover(short_window=2, long_window=3)
    engine = BacktestEngine(data, strat, transaction_cost=0.001, slippage=0.001)
    # also test RSI strategy doesn't crash
    from trading_backtester.strategies.rsi import RSIStrategy
    rsi_strat = RSIStrategy(period=2, lower=20, upper=80)
    engine2 = BacktestEngine(data, rsi_strat)
    results2 = engine2.run()
    assert 'strategy_returns' in results2.columns
    results = engine.run()
    assert 'strategy_returns' in results.columns
    summary = engine.summary()
    assert 'sharpe_ratio' in summary
    assert 'max_drawdown' in summary
    assert 'total_return' in summary
    assert 'cagr' in summary
    assert 'annual_volatility' in summary
