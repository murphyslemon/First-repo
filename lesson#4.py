list2 = []
sl = ["string", "cheese", "pens", "sunglasses"]
print(sl)
sl.insert(3, "4 eggs")
print(sl)
sl.pop(2)
print(sl)
sl.remove("string")
print(sl)
sl.append("banana")
print(sl)
print(sl.index("cheese"))

name = []
name = input("What is your name?")
index = 0
while name != "" and index < len(name):
    print(name[index])
    index += 1

name = []
name = input("What is your name?")
index = 0
for name in range(0):
    print(name[index])
    index += 1

num = 1
while num > 0:
    result = 1
    num = int(input("input a number: "))
    n=num
    while n > 0:
        result *= n
        n -= 1
    if num>0:
        print(result)