import pandas as pd
import yfinance as yf
import numpy as np

# List of tickers
tickers = {
    "NVDA": "Nvidia",
    "PLTR": "Palantir",
    "TSLA": "Tesla",
    "MSFT": "Microsoft",
    "AAPL": "Apple",
    "AMZN": "Amazon",
    "NFLX": "Netflix",
    "GOOGL": "Google",
    "DJI": "Dow Jones Index",
    "^GSPC": "S&P 500",
    "^TNX": "10-Year US Government Bond"
}

# Create an empty DataFrame
df = pd.DataFrame()

# Set start and end dates
start='2010-01-01'
end='2023-06-30'

# Fetch the data
for ticker, name in tickers.items():
    # Get the data from Yahoo Finance
    data = yf.download(ticker, start=start, end=end)
    
    # Select only the adjusted close prices
    adj_close = data['Adj Close']
    
    # Calculate the returns and log returns
    returns = adj_close.pct_change()
    log_returns = np.log(adj_close).diff()
    
    # Add the prices, returns, and log returns to the DataFrame
    df[f'{ticker}_PRC'] = adj_close
    df[f'{ticker}_RET'] = returns
    df[f'{ticker}_LOGRET'] = log_returns

# Drop the missing values
#df = df.dropna()

# Fill missing data with zeros
df = df.fillna(0)

# Drop first line
df = df.drop(df.index[0])

# Write the DataFrame to a CSV file
df.to_csv('DataManagement/daily_data.csv', index_label='DATE')
