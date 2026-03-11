import pandas as pd

class MovingAverageCrossover:
    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = pd.DataFrame(index=data.index)
        df['short_ma'] = data['Close'].rolling(self.short_window).mean()
        df['long_ma'] = data['Close'].rolling(self.long_window).mean()
        df['signal'] = 0
        df.loc[df['short_ma'] > df['long_ma'], 'signal'] = 1
        df.loc[df['short_ma'] < df['long_ma'], 'signal'] = -1
        return df[['signal']]
