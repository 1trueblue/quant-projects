import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
import numpy as np  
import matplotlib.pyplot as plt

endDate= dt.datetime.now()
startDate= endDate - dt.timedelta(days=365*5)
print(endDate, startDate)

stocks = ['MSFT','SPY','QQQ']
df = yf.download(stocks, start=startDate, end=endDate)
print(df.head())

close_prices = df['Close']
print(close_prices.head())

log_returns = np.log(close_prices/close_prices.shift(1))
print(log_returns.head())

cumulative_log_returns = log_returns.cumsum()
cumulative_log_returns.plot(title="Cumulative Returns", figsize=(10,6))

plt.show()