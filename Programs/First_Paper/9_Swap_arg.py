def swap_element(list, arg1, arg2):
    list[arg1], list[arg2] = list[arg2], list[arg1]
    return list


list = [1, 2, 3, 4, 5, 6, 7, 8]
print("original List: ", list)
arg1= 2
arg2= 5
swapped_list = swap_element(list, arg1, arg2)
print("after Swaping index 2 with a 5 : ",swapped_list)  #output:[1, 2, 6, 4, 5, 3, 7, 8]