# Raw Package
import pandas as pd
import datetime as dt
import time
#Data Source
import yfinance as yf

def main():

    stocks = ["TSLA", "TD", "AMZN", "MSFT", "INTC", "GOOG", "INFY", "TCS"]      # Add/Remove stocks as required

    count = 0
    #Using while loop to get the script running for fetching live stocks data at every 30 secs interval
    while True:
        count +=1
        print(f"\n\nScript is executing {count} time")
        data = pd.DataFrame()

        #Interval I use is of 1 minute(change as per requirements)
        for ticker in stocks:
            data[ticker] = yf.download(ticker, period="1d", interval="1m")[['Adj Close']]
            # data = yf.download(tickers="TSLA", period="1d", interval="1m") (for getting a single stock data)
        print("\n", data, "\n\n")
        countdown(30) #time is in secs

#Taken from geekforgeeks.org to place the timer
def countdown(t):

    while t:
        mins, secs = divmod(t, 60) # we can add minutes in timer if required
        timer = '{:02d}'.format(secs)
        print(f"Live data is refreshed at every {timer} seconds", end="\r")
        time.sleep(1)
        t -= 1
        

if __name__ == "__main__":
    main()