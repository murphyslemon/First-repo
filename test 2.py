airports = {"HEL":"Vantaa Airport"}
print(airports)
ICAO_code = input("What is the airports ICAO code: ")
if ICAO_code in airports:
    print(f"{ICAO_code} is {airports[ICAO_code]}.")
else:
    print("not found")