import math
import random

# Phase 1
name = input("What is your name? ")
print("Hello, " + name + "!")

# Phase 2
radius = float(input("Give a radius in meters: "))
area = math.pi * radius ** 2
print(f"The area of that circle is:{area:6.2f}m\u00b2")

# Phase 3
length = float(input("Give the length of a rectangle in metres: "))
width = float(input("Give the width of that rectangle in metres: "))
perimetre = (2*length) + (2*width)
area = length*width
print("The perimeter of that rectangle is: " + str(perimetre) + "m, and the area is: " + str(area) + "m\u00b2")

# Phase 4
print("I will add, multiply and find the average of 3 chosen numbers: ")
one = float(input("Give me your first number: "))
two = float(input("Give me another number: "))
three = float(input("And give me your third number: "))
sum = float(one) + float(two) + float(three)
print("The sum of these numbers is: " + str(sum))
product = float(one) * float(two) * float(three)
print("And the product of these numbers is: " + str(product))
average = (float(one) + float(two) + float(three)) / float(3)
print("The average of these numbers is: " + str(average))

# Phase 5
print("I convert talents, pounds and lots to kilograms.")
talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))
P = float(talent) * float(20) * float(32) * float(13.3)
L = float(pound) * float(32) * float(13.3)
G = float(lot) * float(13.3)
K = (float(P) + float(L) + float(G)) / float(1000)
g = float(K) * float(1000) - (int(K) * float(1000))
print("The total weight in kilograms is: " + str(int(K)) + f"Kg and:{g:6.0f}" + "g")

# Phase 6
print("I will now provide you with a random 3-digit combination for your lock: " + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))
print("I will now provide you with a random 4-digit combination where each number is between 1 and 6: " + str(random.randint(0,6)) + str(random.randint(0,6))+ str(random.randint(0,6)) + str(random.randint(0,6)))
print("Thank you!")