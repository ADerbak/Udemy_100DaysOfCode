import requests

# Calling a basic API
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Check for 200 status. If any issues arise, raise_for_status() will handle it
if not response.raise_for_status():
    data = response.json()
    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']
    print(longitude, latitude)

# Sending API with parameters
response = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}")
if not response.raise_for_status():
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    print(sunrise, sunset)
