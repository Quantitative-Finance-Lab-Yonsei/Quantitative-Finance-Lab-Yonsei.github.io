# data.py

import yfinance as yf
import pandas as pd

def get_sp500():
    """
    Yahoo Finance에서 S&P 500 지수를 1분 단위로 가져온다.
    최근 30개 데이터(약 30분치)만 반환한다.
    """
    ticker = "^GSPC"  # S&P 500 Index 티커
    try:
        data = yf.download(ticker, interval="1m", period="1d", progress=False)
        data.reset_index(inplace=True)
        return data[['Datetime', 'Close']].tail(30)
    except Exception as e:
        print(f"[Error] 데이터 수집 실패: {e}")
        return pd.DataFrame(columns=['Datetime', 'Close'])
