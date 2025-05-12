import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

tickers = ['SPY','BND','GLD','QQQ','VTI']
end_date = datetime.today()
start_date = end_date - timedelta(days= 365*2)

close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end= end_date)
    close_df[ticker] = data['Close']

print (close_df)

output_folder = r"/Users/tejasbakre634/Desktop/project/project1"
output_file = os.path.join(output_folder, 'stock_prices.xlsx')
close_df.to_excel(output_file)