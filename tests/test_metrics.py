import pandas as pd
import numpy as np
import pytest
from trading_backtester import (
    sharpe_ratio,
    max_drawdown,
    total_return,
    compound_annual_growth_rate,
    annual_volatility,
)

def test_sharpe_ratio_constant():
    # constant returns should produce nan Sharpe (zero volatility)
    returns = pd.Series([0.01] * 252)
    sr = sharpe_ratio(returns)
    assert np.isnan(sr)


def test_max_drawdown():
    returns = pd.Series([0.1, -0.2, 0.1, -0.1])
    md = max_drawdown(returns)
    assert md < 0


def test_total_return():
    returns = pd.Series([0.1, 0.2, -0.05])
    tr = total_return(returns)
    assert tr == pytest.approx((1.1 * 1.2 * 0.95) - 1)


def test_cagr_and_volatility():
    returns = pd.Series([0.01] * 252)  # 1 year of constant returns
    cagr = compound_annual_growth_rate(returns)
    vol = annual_volatility(returns)
    # 1% daily returns compound to approximately (1.01**252 - 1) annual
    expected = (1.01 ** 252) - 1
    assert pytest.approx(cagr, rel=1e-6) == expected
    assert pytest.approx(vol, rel=1e-6) == 0.0
