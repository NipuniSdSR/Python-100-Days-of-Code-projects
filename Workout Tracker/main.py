import requests
import os

# -----------Nutritionix-API-details--------------#


APP_ID = os.environ["ENV_NIX_ID"]
API_KEY = os.environ["ENV_NIX_API"]

print(APP_ID,API_KEY)

GENDER = "female"
WEIGHT_KG = "44"
HEIGHT_CM = "154"
AGE = "29"

# Todo: step 1 : print the exercise stats for plain text input.
exercise_input = input("Tell me which exersice you did:")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
response.raise_for_status()
result = response.json()

print(result)
#
# Todo: step 2 : add the exercise details to spread sheet using sheety api.

import datetime as dt

for ex in result["exercises"]:
    date = dt.datetime.now()
    day = date.strftime("%d/%m/%Y")
    time = date.strftime("%X")
    exercise = ex["name"].title()
    duration = ex["duration_min"]
    calories = ex["nf_calories"]

    # print(date)
    # print(day)
    # print(time)
    # print(exercise)
    # print(duration)
    # print(calories)

    sheety_post_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

    sheet_input = {
        "workout": {
            "date": day,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    # Todo: step 3 : Authenticate  Sheety API .
    headers = {
        "Authorization": os.environ.get("ENV_SHEETY_BEARER_AUT")
    }
    response = requests.post(url=sheety_post_endpoint, json=sheet_input, headers=headers)
    print(response.text)
# Todo: step 4 :  Environment Variables  .
