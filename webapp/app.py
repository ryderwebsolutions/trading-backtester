import streamlit as st
import pandas as pd

from trading_backtester import BacktestEngine
from trading_backtester.strategies import (
    MovingAverageCrossover,
    MeanReversion,
    RSIStrategy,
)

st.title("Trading Backtester")

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded is not None:
    data = pd.read_csv(uploaded, parse_dates=True, index_col=0)
else:
    data = pd.read_csv("data/sample.csv", parse_dates=True, index_col=0)

st.write("## Input data")
st.line_chart(data['Close'])

strategy_name = st.selectbox("Strategy", ["ma", "meanrev", "rsi"])

params = {}
if strategy_name == "ma":
    params['short_window'] = st.number_input("Short window", value=20)
    params['long_window'] = st.number_input("Long window", value=50)
elif strategy_name == "meanrev":
    params['window'] = st.number_input("Window", value=20)
    params['threshold'] = st.number_input("Z-threshold", value=1.5)
elif strategy_name == "rsi":
    params['period'] = st.number_input("Period", value=14)
    params['lower'] = st.number_input("Lower threshold", value=30.0)
    params['upper'] = st.number_input("Upper threshold", value=70.0)

transaction_cost = st.slider("Transaction cost", 0.0, 0.01, 0.0, step=0.0001)
slippage = st.slider("Slippage", 0.0, 0.01, 0.0, step=0.0001)

if st.button("Run backtest"):
    if strategy_name == "ma":
        strat = MovingAverageCrossover(**params)
    elif strategy_name == "meanrev":
        strat = MeanReversion(**params)
    else:
        strat = RSIStrategy(**params)

    engine = BacktestEngine(data, strat, transaction_cost=transaction_cost, slippage=slippage)
    results = engine.run()
    summary = engine.summary()

    st.write("### Performance")
    st.json(summary)

    results['equity'] = (1 + results['strategy_returns']).cumprod()
    st.line_chart(results['equity'])
    st.write("### Signals")
    st.line_chart(results['position'])

    st.write("### Returns")
    st.line_chart(results['strategy_returns'])
