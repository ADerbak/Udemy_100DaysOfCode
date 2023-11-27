import datetime
import json

import requests
import os

import user_metrics


# Nutritionix Exercise Stats

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

if not response.raise_for_status():
    response_dict = json.loads(response.text)
    for workout in response_dict["exercises"]:
        exercise = str(workout["name"]).title()
        duration = workout["duration_min"]
        calories = workout["nf_calories"]


        # Sheety - Post to Google Spreadsheet

        sheety_uri = "https://api.sheety.co/2c94b4aabd362e3c421b3193d1f1a5dc/myWorkouts/workouts"

        sheety_headers = {
            "Authorization": f"Bearer {os.environ.get('SHEETY_BEARER_TOKEN')}"
        }

        sheety_data = {
            "workout":{"date": datetime.datetime.today().strftime("%d/%m/%Y"),
              "time": datetime.datetime.today().strftime('%H:%M:%S'),
              "exercise": exercise,
              "duration": duration,
              "calories": calories,
                     }
        }

        response = requests.post(sheety_uri, json=sheety_data ,headers=sheety_headers)
        print(response.text)