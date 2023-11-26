import requests
import secrets

# Create user account
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": secrets.pixela_token,
    "username": secrets.pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.text)
