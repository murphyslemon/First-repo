# problem1
length = float(input("What is the length of your zander in centimeters?"))

if length >= 42:
    print("Congratulations! You have a new pet!")

else:
    print("Boo! Your fish is " + str(42 - length) + "cm too small! Please let it go.")

# problem2
answer = str(input("What is your cabin class??"))
if answer == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif answer == "A":
    print("A: above the car deck, equipped with a window")
elif answer == "B":
    print("B: windowless cabin above the car deck.")
elif answer == "C":
    print("C: windowless cabin below the car deck")
else:
    print("Invalid cabin class")

# problem3
hemoglobin = float(input("What is your hemoglobin level?"))
gender = input("What is your biological gender, male/female?")

if gender == "male":
    if 167 < hemoglobin < 134:
        print("You are unhealthy!")
    else:
        print("You are healthy!")
if gender == "female":
    if 155 < hemoglobin < 117:
        print("You are unhealthy!")
    else:
        print("You are healthy!")

# problem4
year = float(input("Please input a year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year.")
        if year % 400 != 0:
            print("This is not a leap year.")
    if year % 100 != 0:
        print("This is a leap year.")
else:
    print("This is not a leap year.")

