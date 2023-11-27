import requests
import os

import user_metrics

app_id = os.environ.get('NUTRIONIX_APP_ID')
app_key = os.environ.get('NUTRIONIX_APP_KEY')

uri = "https://trackapi.nutritionix.com/v2/natural/exercise"

app_headers = {
    "x-app-id" : app_id,
    "x-app-key" : app_key,
    "Content-Type" : "application/json",
    "x-remote-user-id" : "0"

}

query_params = {
 "query": input("What exercises did you do and for how long? "),
 "gender": user_metrics.my_gender,
 "weight_kg": user_metrics.my_weight,
 "height_cm": user_metrics.my_height,
 "age": user_metrics.my_age
}

response = requests.post(uri, json=query_params, headers=app_headers)
print(response.text)
