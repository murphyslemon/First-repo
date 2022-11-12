import requests
import json
from api_storage import ex12_api_key

# Problem 1
request1 = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(request1).json()
    print(f"Your random and terrible Chuck Norris joke of the day is: \n{response['value']}")
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

# Problem 2
location_name = input("Please enter city name: ")

request2 = "https://api.openweathermap.org/data/2.5/weather?q=" + location_name + "&appid=" + ex12_api_key + "&units=metric"
response2 = requests.get(request2).json()

for a in response2["weather"]:
    print(f"The weather in {location_name} is {a['description']} and the temperature is {response2['main']['temp']} degrees")

