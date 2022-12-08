import requests

api_key = "4cf8cbafaf4798e89f0fa6ceaf78e5c9"
API_ADDRESS = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "q":"Potsdam, United States",
    "appid" : api_key,
}

response = requests.get(url=API_ADDRESS, params=parameters)
response.raise_for_status()

print(response.status_code)

weather_data = response.json()
print(weather_data)

