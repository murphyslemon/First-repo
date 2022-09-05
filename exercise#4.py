#problem 3
l = None
s = None

while True:
   n = input("Please input a number, when finished write done: ")
   if n == "done":
      break

l = None
s = None

command = input ("Please input a number, when finished press enter: ")

while command != "":
    command = input("Please input a number, when finished press enter: ")
num = int(command)

    largest = num if largest < num or largest == None else largest
    smallest = num if smallest > num or smallest == None else smallest

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

# 4th exercise problem 6 - montecarlo method
