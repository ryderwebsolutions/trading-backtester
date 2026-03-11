import pandas as pd

class BacktestEngine:
    def __init__(
        self,
        data: pd.DataFrame,
        strategy,
        transaction_cost: float = 0.0,
        slippage: float = 0.0,
    ):
        """Base backtesting engine.

        Parameters:
        - data: DataFrame with datetime index and at least a 'Close' column.
        - strategy: object implementing `generate_signals(data)` returning a
          DataFrame with a 'signal' column (1 long, -1 short).
        - transaction_cost: cost per trade expressed as fraction of price.
        - slippage: additional cost per trade fraction representing bid/ask
          spread impact.
        """
        self.data = data.copy()
        self.strategy = strategy
        self.transaction_cost = transaction_cost
        self.slippage = slippage
        self.results = None

    def run(self):
        signals = self.strategy.generate_signals(self.data)
        df = self.data.copy()
        df = df.join(signals)
        df['signal'] = df['signal'].fillna(0)
        df['position'] = df['signal'].shift(1).fillna(0)
        df['returns'] = df['Close'].pct_change()
        # apply transaction costs / slippage when position changes
        df['trade_cost'] = (
            (df['position'] - df['position'].shift(1)).abs()
            * (self.transaction_cost + self.slippage)
        )
        df['strategy_returns'] = df['returns'] * df['position'] - df['trade_cost']
        self.results = df
        return df

    def summary(self):
        if self.results is None:
            raise RuntimeError("Backtest not run yet")
        # local import to avoid circular issues during packaging
        from trading_backtester.metrics import (
            sharpe_ratio,
            max_drawdown,
            total_return,
        )
        sr = sharpe_ratio(self.results['strategy_returns'])
        md = max_drawdown(self.results['strategy_returns'])
        tr = total_return(self.results['strategy_returns'])
        return {'sharpe_ratio': sr, 'max_drawdown': md, 'total_return': tr}
