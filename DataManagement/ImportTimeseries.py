import pandas as pd
import yfinance as yf
import numpy as np


def get_data_full():
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
    end='2023-07-01'

    # Fetch the data
    for ticker, name in tickers.items():

        # Get the data from Yahoo Finance
        data = yf.download(ticker, start=start, end=end)
        
        # Select data fields
        open = data['Open']
        high = data['High']
        low = data['Low']
        close = data['Close']
        adj_close = data['Adj Close']
        volume = data['Volume']

        # Manually calculate adjusted open, high, low and volume values
        adj_open = open * adj_close / close
        adj_high = high * adj_close / close
        adj_low = low * adj_close / close
        adj_volume = volume / (adj_close / close)

        # Calculate the returns and log returns based on adjusted close prices
        returns = adj_close.pct_change()
        log_returns = np.log(adj_close/adj_close.shift(1))

        # Add the prices, returns, and log returns to the DataFrame
        df[f'{ticker}_OPEN'] = adj_open
        df[f'{ticker}_HIGH'] = adj_high
        df[f'{ticker}_LOW'] = adj_low
        df[f'{ticker}_CLOSE'] = adj_close
        df[f'{ticker}_VOLUME'] = adj_volume
        df[f'{ticker}_RET'] = returns
        df[f'{ticker}_LOGRET'] = log_returns

    # Fill missing data with zeros
    df = df.fillna(0)

    # Drop first line
    df = df.drop(df.index[0])

    # If ticker is Nvidia then also merge the Nvidia earnings data into the dataframe

    # Read your Nvidia earnings data
    df_nvidia_earnings = pd.read_csv('DataManagement/nvidia_earnings.csv', index_col='DATE', parse_dates=True)

    # Merge the two dataframes
    df = df.merge(df_nvidia_earnings, how='left', left_index=True, right_index=True)

    # Write the DataFrame to a CSV file
    df.to_csv('DataManagement/daily_data.csv', index_label='DATE')


'''
def get_data_simple():
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
'''