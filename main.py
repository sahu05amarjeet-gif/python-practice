import yfinance as yf
import os
tickers = ["RELIANCE.NS", "INFY.NS", "TCS.NS", "TATAMOTORS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "ITC.NS", "WIPRO.NS"]

for ticker in tickers:
    stock = yf.Ticker(ticker)
    data = stock.info 

    current_price = data.get("currentPrice") or data.get("regularMarketPrice") # get() = avoids crashes
    fifty_two_weeks_low = data.get("fiftyTwoWeekLow")
    if current_price is None or fifty_two_weeks_low is None:
        print(f"Skipping {ticker} due to missing data.")
        continue
    trigger_margin = fifty_two_weeks_low * 1.02

    print(f"Current Price: {current_price}")
    print(f"Fifty Two Weeks Low: {fifty_two_weeks_low}")

    if(current_price <= trigger_margin):
        print("ALERT!!! The stock is below 52 weeks low")
        os.system(f'notify-send "{ticker} ALERT!!" "Your Stock is about to hit 52 weeks low point"')

