import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2020-01-01', '2021-12-31', freq='B')
price = 100 + np.cumsum(np.random.randn(len(dates)))
df = pd.DataFrame({'Close': price}, index=dates)
df.to_csv('data/sample.csv')
print(df.head())
print('wrote', len(df), 'rows to data/sample.csv')
