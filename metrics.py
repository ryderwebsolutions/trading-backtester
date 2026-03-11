import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.0):
    # assume returns are daily
    returns = returns.dropna()
    excess = returns - risk_free_rate/252
    if excess.std() == 0 or np.isnan(excess.std()):
        return np.nan
    return np.sqrt(252) * excess.mean() / excess.std()


def max_drawdown(returns):
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = cumulative / peak - 1
    return drawdown.min()


def total_return(returns):
    return (1 + returns).prod() - 1
