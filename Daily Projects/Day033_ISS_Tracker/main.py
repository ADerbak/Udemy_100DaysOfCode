import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if not response.raise_for_status():
    data = response.json()

    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']


