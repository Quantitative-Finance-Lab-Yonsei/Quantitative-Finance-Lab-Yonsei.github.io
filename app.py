import streamlit as st
import FinanceDataReader as fdr
import datetime
import pyupbit


st.set_page_config(layout="wide")
st.title("📈 S&P500 & 이동평균선 차트")

"""
S&P500
"""
Snp_df = fdr.DataReader(360750, datetime.date(2010, 1, 1))
Snp_df['MA20'] = Snp_df['Close'].rolling(window=20).mean()
Snp_df['MA50'] = Snp_df['Close'].rolling(window=50).mean()


"""
Bitcoin
"""
bitcoin_df = pyupbit.get_ohlcv("KRW-BTC")
bitcoin_df['MA20'] = bitcoin_df['Close'].rolling(window=20).mean()
bitcoin_df['MA50'] = bitcoin_df['Close'].rolling(window=50).mean()


"""
Magnificent 7 
"""
AAPL_df = fdr.DataReader("AAPL", datetime.date(2010, 1, 1))
MSFT_df = fdr.DataReader("MSFT", datetime.date(2010, 1, 1))
AMZN_df = fdr.DataReader("AMZN", datetime.date(2010, 1, 1))
NVDA_df = fdr.DataReader("NVDA", datetime.date(2010, 1, 1))
GOOGL_df = fdr.DataReader("GOOGL", datetime.date(2010, 1, 1))
META_df = fdr.DataReader("META", datetime.date(2010, 1, 1))
TSLA_df = fdr.DataReader("TSLA", datetime.date(2010, 1, 1))



st.line_chart(Snp_df[['Close', 'MA20', 'MA50']])
st.line_chart(bitcoin_df[['Close', 'MA20', 'MA50']])
