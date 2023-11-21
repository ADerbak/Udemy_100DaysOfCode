import os

import requests as requests
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple"
CHANGE = ["🔺","🔻"]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize":"compact",
    "apikey": os.environ.get('ALPHA_VANTAGE_API_KEY')
}

results = requests.get(stock_api, params=stock_params)

results_json = results.json()
yesterday_date = next(iter(results_json["Time Series (Daily)"]))
last_price = results_json["Time Series (Daily)"][yesterday_date]
price_diff = float(abs(float(last_price["4. close"])/float(last_price["1. open"])-1))
total_change = int(abs(float(last_price["4. close"])/float(last_price["1. open"])-1)*100)
diff_symbol = CHANGE[0] if float(last_price["4. close"]) > float(last_price["1. open"]) else CHANGE[1]

if price_diff > 0.5:
    # print("Get News!")



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday_date,
        "sortBy": "popularity",
        "apiKey": str(os.environ.get("NEWS_API_KEY"))
    }

    news_results = requests.get(news_api, params=news_params)
    news_results_json = news_results.json()
    for news in news_results_json["articles"][:3]:
        title = news["title"]
        description = news["description"]
        print(STOCK +" "+ diff_symbol + str(total_change) + "%\n" + "Headline:" + STOCK + "\n" + "Brief" + description)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #     .create(
        #     body=STOCK +" "+ diff_symbol + price_diff + "%\n" + "Headline:" + STOCK + "\n" + "Brief" + description,
        #     from_='+18339878049',
        #     to='+13145757071'
        # )
        # print(message.status)

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

