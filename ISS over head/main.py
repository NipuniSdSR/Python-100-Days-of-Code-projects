import requests
from datetime import datetime

import time
import smtplib

my_email = "beecharm.g@gmail.com"
password_g = "frgvefrsveqvcmsf"
receiver_mai = my_email

MY_LAT = 44.666679  # Your latitude
MY_LONG = -74.976929  # Your longitude

def is_iss_above_me():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour > sunset and time_now.hour < sunrise:
        return True


    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    print("Iss checking...")
    if is_night() and is_iss_above_me():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password_g)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Subject: ISS above you🛰️\n\n"
                                    "Hi there,\n ISS is now right above you. \n You may can see it  if you go out now")
