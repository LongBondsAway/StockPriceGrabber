# StockPriceGrabber
#Grabs the stock price for a given ticker


#import required tools/packages
import yfinance as yf

#define the ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2021-1-1', end='2021-4-5')

#see your data
tickerDf

print(tickerDf)
