import random

#problem 1
def func():
    return random.randint(1, 6)

y = func()

while y != 6:
    print(y)
    y = func()
print(y)

#problem 2
def roll(z):
    return random.randint(1, z)

a = int(input("How many sides does your dice have? "))
y = roll(a)

while y != a:
    print(y)
    y = roll(a)
print(y)

#problem 3
x = int(input("How many gallons? "))
y = x * 3.785411784
print(y)
def func():
    x = int(input("How many gallons? "))
    while x >= 0:
        y = x * 3.785411784
        print(y)
        x = int(input("How many gallons? "))

if x >= 0:
    func()

#problem 4
list = []
def func(a):
    print("The sum of the list is: ")
    print(sum(list))

n = int(input("How many numbers will u add to the list: "))
for i in range(n):
    numbers = int(input("Enter a number "))
    list.append(numbers)
func(list)

#problem 5
list = [65, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list2=[]
def func(list):
    if i % 2 == 0:
        list2.append(i)
    return list2
for i in range(len(list) + 1):
    func(list)
print(list2)
print(list)

#problem 6
import math
def ppsm(d, p):
    sm = math.pi * ((d*0.01)/2)**2
    psm = p/sm
    return psm

d1 = float(input("What is the diameter of the first pizza: "))
p1 = float(input("What is the price of the first price: "))
d2 = float(input("What is the diameter of the second pizza: "))
p2 = float(input("What is the price of the second pizza: "))

a = ppsm(d1, p1)
b = ppsm(d2, p2)

if a > b:
    print("The second pizza is cheaper.")
if a < b:
    print("The first pizza is cheaper.")
if a == b:
    print("They are both the same price.")