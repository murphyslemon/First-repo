# #problem 1
seasons_of_the_year = ("summer", "summer", "autumn", "autumn", "autumn", "winter", "winter", "winter", "spring", "spring", "spring", "summer")
season_number = int(input("Enter the month number(1-12): "))
season = seasons_of_the_year[season_number - 1]
print(f"Month number {season_number} is {season} in the southern hemisphere.")

# #problem 2
names = set()
n = "ajdhf"
while n != "":
    n = input("Enter a name: ")
    if n in names:
        print("Existing name")
    if n not in names:
        print("New name")
    names.add(n)
names.remove("")

print("The names in the list are: ")
[print(i) for i in names]

#problem 3
airports = {}
while True:
    select = int(input("Enter what option you want to do. (1-3) \n1. Enter new airport\n2. Fetch existing airport\n3. Quit\nWhat do you want to do: "))
    if select == 1:
        airport_name = input("What is the airport name: ")
        ICAO_code = input("What is the airport ICAO code: ")
        airports[ICAO_code] = airport_name

    elif select == 2:
        ICAO_code = input("What is the airports ICAO code: ")
        if ICAO_code in airports:
            print(f"{ICAO_code} is {airports[ICAO_code]}.")
        else:
            print("not found")
    elif select == 3:
        break
    else:
        print("Error, wrong input:")