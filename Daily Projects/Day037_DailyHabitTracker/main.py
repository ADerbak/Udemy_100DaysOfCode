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

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@aderbak , it is your profile page!","isSuccess":true}

pixela_graph_endpoint = f"{pixela_endpoint}/{secrets.pixela_username}/graphs"

graph_config = {
    "id": "reading",
    "name" : "Pages Read Tracker",
    "unit" : "Pages",
    "type" : "int",
    "color": "ajisai"
}

pixela_header = {"X-USER-TOKEN": secrets.pixela_token}

response = requests.post(pixela_graph_endpoint, json=graph_config, headers=pixela_header)
print(response.text)
# {"message":"Success.","isSuccess":true}