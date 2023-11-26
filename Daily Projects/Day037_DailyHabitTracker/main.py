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


# Create a new graph
pixela_graph_endpoint = f"{pixela_endpoint}/{secrets.pixela_username}/graphs"

graph_config = {
    "id": "reading",
    "name" : "Pages Read Tracker",
    "unit" : "Pages",
    "type" : "int",
    "color": "ajisai"
}

pixela_header = {"X-USER-TOKEN": secrets.pixela_token}

# response = requests.post(pixela_graph_endpoint, json=graph_config, headers=pixela_header)
# print(response.text)
# {"message":"Success.","isSuccess":true}

# Post a value to the graph
pixela_value_endpoint = f"{pixela_graph_endpoint}/reading"

value_config = {
    "date": "20231125",
    "quantity": "40",
    "optionalData": "{\"Books\": \"Moonwalking with Einstein\"}"
}

# response = requests.post(pixela_value_endpoint, json=value_config, headers=pixela_header)
# print(response.text)

# Update a value

pixela_value_endpoint_update = f"{pixela_value_endpoint}/20231125"

updated_value_config = {
    "quantity": "100",
    "optionalData": "{\"Books\": \"Moonwalking with Einstein\"}"
}

response = requests.put(pixela_value_endpoint_update, json=updated_value_config, headers=pixela_header)
print(response.text)
