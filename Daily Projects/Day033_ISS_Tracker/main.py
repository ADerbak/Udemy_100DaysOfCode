import requests

response = requests.get(url="http://api.open-notify.org/iss.json")
print(response)