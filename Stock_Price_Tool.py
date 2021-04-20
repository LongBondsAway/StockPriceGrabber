#Stock Price Grabber
breakpoint()

#import required tools/packages
import yfinance as yf
import sys
import click

#define variables
ticker = sys.argv[1]
period = sys.argv[2]
start_date = sys.argv[3]
end_date = sys.argv[4]

#get data on this ticker
tickerData = yf.Ticker(ticker)

#get the historical prices for this ticker
tickerDf = tickerData.history(period, start_date, end_date)

#see your data
tickerDf

click.echo(tickerDf)

#Input validation
if len(sys.argv) > 1:
    for arg in sys.argv:
        click.echo(arg)
else:
    click.echo('No arguments found')
