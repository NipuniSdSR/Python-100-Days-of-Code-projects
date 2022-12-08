import requests
# To send sms we use Twilio module
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


#-----------------Requests---------------------------------#
api_key = "69f04e4613056b159c2761a9d9e664d2"
LONGITUDE = 106.865036 #-74.976929
LATITUDE = -6.175110 #44.666679
API_ADDRESS = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}


#------------Twilio----------------------------------------#
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC2b57d41f77f1c697bc80083ca8c80185"
auth_token = os.environ.get("Auth_token")


#-----------------------------------------------------------#

response = requests.get(url=API_ADDRESS, params=parameters)
response.raise_for_status()

print(response.status_code)

weather_data = response.json()



first_12_hours = weather_data["hourly"][:12]  # list that has dictionaries as items

# print(first_12_hours)

will_rain = False
for hour in first_12_hours:
    condition_code = hour["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. remember to bring an umbrella",
        from_="+12513254820",
        to="+1"+os.environ.get("MY_NUMBER")
    )
    print(message.status)

# to run the code automatically at 7am use "https://www.pythonanywhere.com/"M