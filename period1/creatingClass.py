import math
class Pizza:
    def __init__(self, diameter, price):
        self.diameter = diameter
        self.price = price
    def __str__(self):
        return f"the diameter of my pizza is {self.diameter}cm " \
               f"and the price is ${self.price} " \
               f"and the price per square meter is {self.pricePerSquareMeter()}"
    def pricePerSquareMeter(self):
        sm = math.pi * ((self.diameter * 0.01)/2)**2
        return self.price/sm

def sortPizza(pizza):
    return pizza.pricePerSquareMeter()

pizzalist = [Pizza(1, 1), Pizza(2, 2), Pizza(3, 6)]
pizzalist.sort(key = sortPizza)

for pizza in pizzalist:
    print(pizza)
# d1 = Pizza(0, 0)
# d1.diameter = float(input("What is the diameter of the first pizza: "))
# d1.price = float(input("What is the price of the first price: "))
#
# print(d1)

#d2 = float(input("What is the diameter of the second pizza: "))
#p2 = float(input("What is the price of the second pizza: "))

#a = ppsm(d1, p1)
#b = ppsm(d2, p2)
#
# if a > b:
#     print("The second pizza is cheaper.")
# if a < b:
#     print("The first pizza is cheaper.")
# if a == b:
#     print("They are both the same price.")