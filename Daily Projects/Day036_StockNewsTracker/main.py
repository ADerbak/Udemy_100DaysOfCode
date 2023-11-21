import os

import requests as requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api = "https://www.alphavantage.co/query"
# ?function=TIME_SERIES_DAILY&symbol={{SYMBOL}}&outputsize=compact&apikey={{ALPHA_VANTAGE_KEY}}
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize":"compact",
    "apikey": os.environ.get('ALPHA_VANTAGE_API_KEY')
}

results = requests.get(api, params=stock_params)

results_json = results.json()
yesterday_date = next(iter(results_json["Time Series (Daily)"]))
last_price = results_json["Time Series (Daily)"][yesterday_date]
price_diff = float(abs(float(last_price["4. close"])/float(last_price["1. open"])-1))

if price_diff > 0.5:
    print("Get News!")
else:
    print("{:.2f}".format(price_diff) + " change, no news")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

