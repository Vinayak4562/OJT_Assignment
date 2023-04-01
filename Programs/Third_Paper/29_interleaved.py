# def interleave(iterable1, iterable2):   
#     iterator1 = iter(iterable1)       # Get iterators for the two input iterable1
#     iterator2 = iter(iterable2)       # Get iterators for the two input iterable2
    
#     while True:                       # Loop until both iterators are exhausted
#         try:           
#             yield next(iterator1)     # Yield an item from the first iterable
#         except StopIteration:
#             break                     # First iterable is exhausted, break out of loop

#         try:            
#             yield next(iterator2)     # Yield an item from the second iterable
#         except StopIteration:            
#             break                     # Second iterable is exhausted, break out of loop

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8, 9]

# interleaved = interleave(list1, list2)

# for item in interleaved:
#     print(item)



# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 5, 55, 66] 
# list3 = [] 
# iter1 = iter2 = 0  
# while iter1 < len(list1) and iter2 < len(list2):
#     list3 += [list1[iter1]]
#     iter1 += 1
#     list3 += [list2[iter2]]
#     iter2 += 1

# if iter1 < len(list1):
#     list3 += list1[iter1:]
# if iter2 < len(list2):
#     list3 += list2[iter2:]

# print(list3)



# start = end= 0
# while start < len(list1) and end < len(list2):
#     if list1[start] < list2[end]:
#         list3.append(list1[start])
#         start += 1
#     else:
#         list3.append(list2[end])
#         end +=1
# if start < len(list1):
#     list3.extend(list1[start:])
# if end < len(list2):
#     list3.extend(list2[end:])
# print(list3)


def interleave(list1,list2):
    return iter(sum(zip(list1,list2),()))

print(list(interleave([1,2,3,4],[1,2,3,4,5,6])))