# #problem 1
# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.
#
# season = ('spring', 'summer', 'autumn', 'winter')
# season
# input("What month is it? ")
#
# #problem 2
# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or
# Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.

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