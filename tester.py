import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download Apple's stock data for the past year
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")

# Step 2: Calculate daily returns
data['Daily Returns'] = data['Close'].pct_change()

# Step 3: Print the first few rows of the data
print("First 5 rows of the data:")
print(data[['Close', 'Daily Returns']].head())

# Step 4: Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='AAPL Closing Price', color='blue')
plt.title("Apple (AAPL) Closing Prices - Past Year")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()