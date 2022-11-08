import requests, json

#Problem 1
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])

#Problem 2