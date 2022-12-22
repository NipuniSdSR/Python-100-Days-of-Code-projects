from twilio.rest import Client
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# TODO: Twillow verification code
"""
1oOcdKuThEIKBCKfWq2P9QEbmuMHten_1tc9VS0k
"""

today = dt.datetime.now()
yesterday = today.replace(day=today.day - 1, hour=16, minute=0, second=0).strftime("%Y-%m-%d %H:%M:%S")  # string
day_before_yesterday = today.replace(day=today.day - 2, hour=16, minute=0, second=0).isoformat(sep=" ",
                                                                                               timespec="seconds")

# ------------Twilio----------------------------------------#
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC2b57d41f77f1c697bc80083ca8c80185"
auth_token = "1bcf0e27ebb947faa15f03cc8a8deda0"

# TODO: # STEP 1: Use https://www.alphavantage.com
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# --------------alphavantage --------------------------------#
API_key_stock = "ZSP2TR39EFVV01EJ"
API_address_stock = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": API_key_stock,
}

response = requests.get(API_address_stock, params=parameters)
response.raise_for_status()
print(response.status_code)
stock_data = response.json()["Time Series (60min)"]

yesterday_stock_data = stock_data[yesterday]
day_before_yesterday_stock_data = stock_data[day_before_yesterday]

yesterday_stock_price = float(yesterday_stock_data["4. close"])
day_before_yesterday_stock_price = float(day_before_yesterday_stock_data["4. close"])

percentage = round((yesterday_stock_price - day_before_yesterday_stock_price) / yesterday_stock_price * 100)
print(percentage)
up_down = 0
if percentage > 0:
    up_down = f"🔺{percentage}%"
else:
    up_down = f"🔻{percentage}%"


# if percentage >= 5 or percentage <= -5:
#     print("Get News")


# TODO: # STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# --------------newsapi --------------------------------#

API_key_news = "7c3ab6b4947340558435c94fe21d1395"
API_address_news = "https://newsapi.org/v2/everything"
parameters = {
    "q": COMPANY_NAME,
    "from": yesterday[:10],
    "sortBy": "popularity",
    "apiKey": API_key_news,
}

if abs(percentage)>5:
    response = requests.get(API_address_news, params=parameters)
    response.raise_for_status()
    print(response.status_code)

    news_data = response.json()["articles"][:3]

    # formating articles

    formatted_articles = [f"TSLA: {up_down}\n"
                 f"Headline: {news['title']}\n"
                 f"Brief: {news['description']}" for news in news_data]

    # TODO: # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    client = Client(account_sid, auth_token)
    for news in formatted_articles:
        message = client.messages.create(
            body= news,
            from_="+12513254820",
            to="+1***********"
        )

        print(message.status)

# TODO: Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
