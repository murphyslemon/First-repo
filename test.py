list = [65, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list2=[]
def func(list):
    if i % 2 == 0:
        list2.append(i)
    return list2

for i in range(len(list)):
    func(list)
print(list2)
print(list)
