import pandas as pd

class MeanReversion:
    def __init__(self, window=20, threshold=1.5):
        self.window = window
        self.threshold = threshold

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = pd.DataFrame(index=data.index)
        df['rolling_mean'] = data['Close'].rolling(self.window).mean()
        df['rolling_std'] = data['Close'].rolling(self.window).std()
        zscore = (data['Close'] - df['rolling_mean']) / df['rolling_std']
        df['signal'] = 0
        df.loc[zscore > self.threshold, 'signal'] = -1
        df.loc[zscore < -self.threshold, 'signal'] = 1
        return df[['signal']]
