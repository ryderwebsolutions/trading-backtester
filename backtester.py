import pandas as pd

class BacktestEngine:
    def __init__(self, data: pd.DataFrame, strategy):
        """data: DataFrame with at least a 'Close' column and datetime index
        strategy: object with generate_signals method returning DataFrame with 'signal' column"""
        self.data = data.copy()
        self.strategy = strategy
        self.results = None

    def run(self):
        signals = self.strategy.generate_signals(self.data)
        df = self.data.copy()
        df = df.join(signals)
        df['signal'].fillna(0, inplace=True)
        df['position'] = df['signal'].shift(1).fillna(0)
        df['returns'] = df['Close'].pct_change()
        df['strategy_returns'] = df['returns'] * df['position']
        self.results = df
        return df

    def summary(self):
        if self.results is None:
            raise RuntimeError("Backtest not run yet")
        from .metrics import sharpe_ratio, max_drawdown, total_return
        sr = sharpe_ratio(self.results['strategy_returns'])
        md = max_drawdown(self.results['strategy_returns'])
        tr = total_return(self.results['strategy_returns'])
        return {'sharpe_ratio': sr, 'max_drawdown': md, 'total_return': tr}
