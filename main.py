import os
import requests
from datetime import datetime

GENDER = "Male"
WEIGHT = os.getenv("WEIGHT")

HEIGHT = 160
AGE = 20


SHEETY_USERNAME =os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD =os.getenv("SHEETY_PASSWORD")
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")


ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}


response = requests.post(ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(result)

url_sheety = "https://api.sheety.co/4362aec20002f3621873feb3b1e3b061/myWorkouts/workouts"
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%Y-%m-%d")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(
  url_sheety,
  json=sheet_inputs,
  auth=(
      SHEETY_USERNAME,
      SHEETY_PASSWORD,
  )
)

#sheet_response = requests.post(url_sheety, json=sheet_inputs)
print(sheet_response.text)
