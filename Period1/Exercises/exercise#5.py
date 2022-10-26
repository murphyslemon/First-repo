#problem 1
import random
list = []
dice = input("How many dice will you roll? ")

for n in range(int(dice)):
    x = random.randint(1, 6)
    list.append(x)

print("The sum of the " + str(dice) + " dice is equal to " + str(sum(list)))

#problem 2
list = []
n = input("Give a number: ")
while n != "":
    list.append(int(n))
    n = input("Give a number: ")

list.sort(reverse=True)
print("The largest 5 of the numbers given are: " + str(list[:5]))

#problem 3
n = input("Input an integer number: ")
half = int(n) // 2
if int(n) > 1:
    for i in range (2, int(half+1)):
        if (int(n) % i) == 0:
            print(n, "is not a prime number.")
            break
    else:
        print(n, "is a prime number.")
else:
    print(n, "is not a prime number")

#problem 4
list = []
for i in range(5):
    list.append(input("Please give 5 cities (Press enter after each one): "))
for i in range(5):
    print(list[i])