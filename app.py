import streamlit as st
import FinanceDataReader as fdr
import datetime

st.set_page_config(layout="wide")
st.title("📈 S&P500 & 이동평균선 차트")

df = fdr.DataReader(360750, datetime.date(2010, 1, 1))
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
st.line_chart(df[['Close', 'MA20', 'MA50']])
