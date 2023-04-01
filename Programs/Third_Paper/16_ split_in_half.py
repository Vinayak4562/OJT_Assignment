def split_in_half(list1):
    length = len(list1)
    mid = length // 2
    first_half = list1[:mid]
    second_half = list1[mid:]
    print(first_half,second_half)       # return first_half, second_half


list1 = [1,2,3,4,5,6]
print(split_in_half(list1))
print(type(split_in_half))
print(split_in_half([1, 2, 3, 4]))

# Out-Put: ([1, 2], [3, 4]) 


