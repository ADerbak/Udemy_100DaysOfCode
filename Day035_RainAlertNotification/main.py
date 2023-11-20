import requests as requests

from secrets import app_id, lat, long


api = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&exclude=hourly,daily&appid={app_id}"
result = requests.get(api)
print(result.text)