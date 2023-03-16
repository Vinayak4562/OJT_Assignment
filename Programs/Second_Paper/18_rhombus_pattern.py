
n = int(input("Enier the Number: "))

for i in range(1, n+1):             # print upper half of the Rhombus   
    for j in range(i, 0, -1):       # print numbers in descending order
        print(j, end="")
   
    for j in range(2, i+1):          # print numbers in ascending order
        print(j, end="")
    print()


for i in range(n-1, 0, -1):          # print lower half of the Rhombus 
    
    for j in range(i, 0, -1):       # print numbers in descending order
        print(j, end="")
    
    for j in range(2, i+1):         # print numbers in ascending order
        print(j, end="")
    print()
