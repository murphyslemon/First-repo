import math


def hello():
    print("Hello Wolrd")
    for i in range(2):
        print("------------")
    print("Goodbye World")
    return

hello()
print("blah blah blah")
hello()

def minus(arguement):
    if arguement > 0:
        return -arguement
    else:
        return arguement

number = int(input("Give a number: "))
while number != 0:
    print(minus(number))
    number = int(input("Give a number: "))

verifun1 = minus(4)
verifun2 = math.sqrt(4)

#newton rapture to understand this square root calculator
def sqr(a):
    x = a/2
        #some code to estimate square root was copied here
    return x

def plus(a,b):
    return a+b

result = plus (2,3)
print(f"{result}")

def change(city):
    print("At the beginning of the function: " + city)
    city = "Vantaa"
    print("At the end of the function: " + city)
    return

city = "Helsinki"
print("At the beginning in the main program: " + city)
change(city)
print("At the end of the main program: " + city)

