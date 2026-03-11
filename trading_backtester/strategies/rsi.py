import pandas as pd

class RSIStrategy:
    def __init__(self, period=14, lower=30, upper=70):
        self.period = period
        self.lower = lower
        self.upper = upper

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = pd.DataFrame(index=data.index)
        delta = data['Close'].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(self.period).mean()
        avg_loss = loss.rolling(self.period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        df['signal'] = 0
        df.loc[rsi < self.lower, 'signal'] = 1
        df.loc[rsi > self.upper, 'signal'] = -1
        return df[['signal']]
