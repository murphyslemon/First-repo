#Write a program for fetching and storing airport data. 
#The program asks the user if they want to enter a new airport, 
# fetch the information of an existing airport or quit. 
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code 
# and name of the airport. If the user chooses to fetch airport information instead, 
# the program asks for the ICAO code of the airport and prints out the corresponding name. 
# If the user chooses to quit, the program execution ends. 
# The user can choose a new option as many times they want until they choose to quit. 
# (The ICAO code is an identifier that is unique to each airport. For example, 
# the ICAO code of Helsinki-Vantaa Airport is EFHK. 
# You can easily find the ICAO codes of different airports online.)

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