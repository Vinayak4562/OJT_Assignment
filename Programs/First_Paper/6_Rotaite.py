list= [10, 20, 30, 40, 50, 60, 70]
n=3
# Using Slicing method
  
# list1= list[0:n+1]
# list2= list[(n+1):len(list)]
# list = list2 + list1
# print("list1",list1)   
# print("list2",list2)
# print("list",list)

# Using right_rotate functios 

def right_rotate(list, n):                        # Right rotate list lst by n positions.    
    index = len(list) - n                         # Calculate the index where the rotation starts.
    return list[index:] + list[:index]    # Perform the rotation
    

rotated_list = right_rotate(list, n)
print(rotated_list)