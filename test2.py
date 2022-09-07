#problem 4
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
