#Control statements are used for control the flow of execution, here 2 contril statemennts/loops
# 1. FOR LOOP :if we know the  start and end value we should use for loop.
# 2.WHILE LOOP:if we dont know the  start and end value we should use while loop.
# for  variable in range (start_value, end_value,step_value)
a = [1,2,3,4,5,6]
for i in range (len(a)):
    print(a[i], end=" ")
print()

for i in range (0,3):
    print(a[i], end=" ")
print()

for i in range (0,len(a),2):
    print(a[i], end=" ")
print()

for i in range (0,4,2):
    print(a[i], end=" ")
print()

# for i in range (::-1):
#     print(a[i], end=" ")
# print()

# ----------WHILE LOOP---------
i = 1
while i < 10:
    print(i, end=" ")
    i+= 1
print()

i=0
l = [6,2,1,8,5,4,6,9,8,5,3,2,4]
while i < len(l):
    print(l[i], end=" ")
    i+= 1
print()
