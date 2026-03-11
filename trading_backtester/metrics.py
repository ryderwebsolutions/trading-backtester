import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.0):
    returns = returns.dropna()
    excess = returns - risk_free_rate / 252
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


def compound_annual_growth_rate(returns):
    """Calculate CAGR from a series of periodic returns (assumed daily)."""
    returns = returns.dropna()
    periods = returns.shape[0]
    if periods == 0:
        return np.nan
    total_ret = (1 + returns).prod()
    years = periods / 252
    if years <= 0:
        return np.nan
    return total_ret ** (1 / years) - 1


def annual_volatility(returns):
    returns = returns.dropna()
    return returns.std() * np.sqrt(252)
