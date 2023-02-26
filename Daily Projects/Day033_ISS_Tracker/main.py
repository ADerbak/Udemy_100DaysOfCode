import requests
import datetime

# Calling a basic API
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Check for 200 status. If any issues arise, raise_for_status() will handle it
if not response.raise_for_status():
    data = response.json()
    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']
    print(longitude, latitude)

# Sending API with parameters
response = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0")
if not response.raise_for_status():
    data = response.json()
    sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
    sunset = data['results']['sunset'].split("T")[1].split(":")[0]
    print(sunrise, sunset)

time_now = datetime.datetime.now().hour

print(time_now)



