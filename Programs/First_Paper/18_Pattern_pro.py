# n = int(input("Enter the number of rows: "))
import time
n = 10
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
    start_time = time.time()
    while time.time() - start_time < 7200:   # 2 hours * 3600 seconds per hour
        pass

