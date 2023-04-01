def interleave(a, b):
    result=[]                       # This empty list is used to append the elements of list a and list b
    if len(a) < len(b):             # here we will check for the lenth of the smallest lest
        for i in range (len(a)):    # if list a is less than list b it will run the loop till lenth if the list a 
            result.append(a[i])
            result.append(b[i])
    else:                           # if list a is greater than or equal to list b it will run the loop till lenth if the list b 
        for i in range (len(b)):
            result.append(a[i])
            result.append(b[i])            
#     return result

# def interleave(a, b):                   #Interleave two iterables
#     result = []
#     for item1, item2 in zip(a, b):     # zip function is used to pair up the elements of the two iterables. 
#         result.append(item1)
#         result.append(item2)
#     return result


a = [1, 2, 3, 4, 5 ]
b = ['a', 'b', 'c','d']
result = interleave(a, b)
print(result)  # Output: [1, 'a', 2, 'b', 3, 'c', 4, 'd']
