#problem 1
n = 1
while n <= 1000:
    if n % 3 ==0:
        print(n)
    n=n+1

#problem2
inches = int(input("Input inches: "))
while inches >= 0:
    print(inches * 2.54)
    inches = int(input("Input inches: "))
    if inches < 0:
        break


#problem 3
n = int(input("Please input a number, when finished press enter: "))
l = n
s = n

while n != "":
    temp = input("Please input a number, when finished press enter: ")
    if temp == "":
        break
    else:
        n = int(temp)
    if n > l:
        l = n
    if n < s:
        s = n

print("largest: ", l)
print("smallest: ", s)

#problem 4
import random
n = random.randint(0,10)
g = int(input("What is your guess: "))

if g > n:
    while g != n:
        print("Lower")
        g = int(input("What is your next guess: "))
if g<n:
    while g != n:
        print("Higher")
        g = int(input("What is your next guess: "))
if g == n:
    print("You are a legend!")

#problem 5
username = "python"
password = "rules"

answer1 = input("username: ")
answer2 = input("password: ")
n = 1

while answer1 != username and answer2 != password:
    if n <= 5:

        answer1 = input("username: ")
        answer2 = input("password: ")
        n = n+1
    if n >=5: print("Access denied")
    break
else:
    print("Welcome")

#problem 6
import random

N = int(input("Give the number of random points: "))
count = 0
circle = 0
square = 0

while count != N:
    count = count + 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    n = x ** 2 + y ** 2
    if n < 1:
        circle = circle + 1

pi = 4*circle/N
print("pi: " + str(pi))

