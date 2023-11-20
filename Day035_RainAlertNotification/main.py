import requests as requests

from secrets import app_id, lat, long

# api = f"https://api.openweathermap.org/data/3.0/onecall"
api = f"https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lat": lat,
    "lon": long,
    "appid": app_id,
    # "exclude": "daily,current,minutely"

}

response = requests.get(api, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

# find if <7xx code called in hourly.weather.id for the next 12 id's
for i in range(0, 12):
    hourly_weather=weather_data.hourly[i]
    print(hourly_weather.weather.id)
    if hourly_weather.weather[0].id < 700:
        print("Bring an umbrella! Bad weather in next 12 hours")
        break



