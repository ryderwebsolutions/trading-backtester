import pandas as pd
import numpy as np
from metrics import sharpe_ratio, max_drawdown, total_return

def test_sharpe_ratio_constant():
    returns = pd.Series([0.01] * 252)
    sr = sharpe_ratio(returns)
    assert sr == pytest.approx(np.sqrt(252) * 0.01 / 0)


def test_max_drawdown():
    returns = pd.Series([0.1, -0.2, 0.1, -0.1])
    md = max_drawdown(returns)
    assert md < 0


def test_total_return():
    returns = pd.Series([0.1, 0.2, -0.05])
    tr = total_return(returns)
    assert tr == pytest.approx((1.1 * 1.2 * 0.95) - 1)
