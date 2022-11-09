import requests, json

#Problem 1
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])

#Problem 2
location_name = input("Please enter city name, state code or country code: ")
request2 = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"
#weather from lat and long
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

#lat and long convert to city name
http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

api key?
873df6e3e029ba2d8538f1482461817f