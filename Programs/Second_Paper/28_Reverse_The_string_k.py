# def reverse_every_2k(s, k): 
#     lst = list(s)                               # Convert the string to a list of characters (since strings are immutable)    
#     n = len(lst)
       
#     for i in range(0, n, 2*k):                  # Iterate over each 2k chunk of the list
#         j = min(i + k, n) - 1                   # Reverse the first k characters in the chunk (or all of them if there are fewer than k)
#         for m in range(i, i + (j - i + 1) // 2):
#             lst[m], lst[j - (m - i)] = lst[j - (m - i)], lst[m]

#     return ''.join(lst)                         # Convert the list back to a string and return it

# s = input("Enter the string: ")
# k = int(input("Enter the Value of k: "))
# obj = reverse_every_2k(s,k)
# print(obj)

a = input("Enter the string: ")
a = list(a)
n = len(a)
k = 2
for i in range(0,n,2*k):
    start = i
    end = min(i+k-1, n-1)
    while start<end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
print("2 K reverse is:","".join(a))

