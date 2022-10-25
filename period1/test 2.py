seasons_of_the_year = ("Spring", "Summer", "Autumn", "Winter")
month = ([3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2])

print(len(month))
month_number = int(input("Enter the month number(1-12): "))

for i in range(len(month)):
    if month_number in month[i]:
        print(seasons_of_the_year[i])
