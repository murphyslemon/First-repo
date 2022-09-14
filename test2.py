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
