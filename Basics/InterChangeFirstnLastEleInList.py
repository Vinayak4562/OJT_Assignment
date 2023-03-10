# Interchange first and last elements Knowing the last element index value.
l = [1,2,3,4,5,6,7,8,9]
print("Before changing the ele: ", l)
l[0], l[8]=l[8],l[0]
print("After changing the ele: ", l)


# Interchange first and last elements taking temp variable.
l1 = [1, 2, 3, 4, 5]  
print("Before changing the ele: ", l1)
temp = l1[0]
l1[0] = l1[-1]
l1[-1] = temp
# l1[0], l1[-1] = l1[-1], l1[0] using one line code.
print("after changing the ele: ", l1)