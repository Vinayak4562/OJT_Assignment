def tail(seq, n):
    if n <= 0:
        return []
    else:
        return f'Last n number elements from the list : , {seq[-n:]}'

seq = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]
n = int(input("Enter the Value of n :"))
print(tail(seq,n))

# Out-Put: [3, 4, 5]
