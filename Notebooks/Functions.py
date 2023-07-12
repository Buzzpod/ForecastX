import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import mplfinance as mpf
import matplotlib.dates as mdates
import matplotlib.lines as mlines

month_year_formatter = mdates.DateFormatter('%Y-%m') # The "," is intentional.
locator = mdates.MonthLocator(interval=3)

def tsPlot(data, company, data_type):

    # Plot the NVDA log return series
    fig, ax = plt.subplots(figsize=(20,10))

    # Change figure facecolor (area surrounding the plot)
    fig.patch.set_facecolor('white')

    # Change plot facecolor (actual plot background)
    ax.set_facecolor('whitesmoke')

    # Change axes color
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.title.set_color('black')

    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')

    ax.plot(data, color='royalblue')

    X = plt.gca().xaxis
    X.set_major_locator(locator)
    X.set_major_formatter(month_year_formatter)

    fig.autofmt_xdate()

    plt.title(f'{company} {data_type} Series')
    plt.xlabel('Date')
    plt.ylabel(data_type)
    plt.grid(True, color='white')
    plt.show()


def candlestickPlot(data, company):
    # Define Moving Average parameters
    mav_titles = ['MA10','MA20','MA30']
    mavs = [10,20,30]
    colors = ['b', 'g', 'r']

    # Create a custom style to increase figure size
    mc = mpf.make_marketcolors(up='g',down='r')
    s = mpf.make_mpf_style(marketcolors=mc)
    s['figure.facecolor'] = 'lightgray'

    # Add MAV and volume to the plot
    apds = [mpf.make_addplot(data['Close'].rolling(mav).mean(), color=color) for mav, color in zip(mavs, colors)]

    # Create the plot
    fig, axes = mpf.plot(data, type='candle', style=s, addplot=apds, title=f'{company} Stock Price',
                        ylabel='Price ($)', figsize=(20,10), volume=True, returnfig=True)

    # Create custom legend
    lines = [mlines.Line2D([], [], color=color) for color in colors]
    axes[0].legend(lines, mav_titles, loc='upper left')