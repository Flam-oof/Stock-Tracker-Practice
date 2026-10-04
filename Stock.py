import streamlit as st
import yfinance as yf
import pandas as pd

st.title("我的台股與 ETF 追蹤")

symbols = ["00935.TW", "00981A.TW", "00993A.TW", "2330.TW"] #追蹤的股票或 ETF 代碼

rows = []
for s in symbols:
    data = yf.Ticker(s).history(period="5d")
    today = data["Close"].iloc[-1]
    yesterday = data["Close"].iloc[-2]
    change = (today - yesterday) / yesterday * 100
    rows.append({"代碼": s, "收盤價": round(today, 2), "漲跌幅(%)": round(change, 2)})

table = pd.DataFrame(rows)
st.dataframe(table)

st.subheader("近 5 日漲跌幅走勢 (%)")
prices = pd.DataFrame({s: yf.Ticker(s).history(period="5d")["Close"] for s in symbols})
percent = (prices / prices.bfill().iloc[0] - 1) * 100
st.line_chart(percent)