#problem 3
l = None
s = None

while True:
   n = input("Please input a number, when finished write done: ")
   if n == "":
      break

l = None
s = None

command = input ("Please input a number, when finished press enter: ")

while command != "":
    command = input("Please input a number, when finished press enter: ")
num = int(command)

    largest = num if largest < num or largest == None else largest
    smallest = num if smallest > num or smallest == None else smallest
