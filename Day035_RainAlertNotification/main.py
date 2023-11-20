import requests as requests

from secrets import app_id, lat, long

api = f"https://api.openweathermap.org/data/3.0/onecall"
weather_params = {
    "lat": lat,
    "long": long,
    "app_id": app_id,
    "exclude": "daily,current,minutely"

}

response = requests.get(api, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)


