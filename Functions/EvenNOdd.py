# list = list(input("enter the input: "))
list = [2,3,4,5,6,7,8,9]
print(list)
even = 0
odd = 0
l1 = []
l2 = []
i = 0
for i in list:
    if i%2 == 0:
        even += 1
        l1.append(i)
    else:
        odd += 1
        l2.append(i)
print("even:{} and odd:{}".format(even,odd))

print("even list: ", l1)
print("odd list: ", l2)