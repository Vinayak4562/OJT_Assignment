# collection is nothing but a collecting a group of defferant type of data in a comman place 
# here we have  5 types of coll.
# list, tuple, set, dictionary, string.

# 1.LIST:Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# l1 = [1,2,3,4,5,6]
# l2 = [1,2,3]
# print(len(l1))
# l1.append(7)
# print("Append: ",l1)
# l1.append([1,2,3]) #its alow us to append list insid a list.
# print("Append list: ",l1)
# l1.insert(1,22) #Insert the value 22 as the second element of the l1 list,
# print("insert: ",l1)       # it will start counting 1 not for 0.
# l1.clear() #it will clear all the list.
# print("clear list: ",l1)
# l1 = l2.copy() #it will copy the l2 to l1.
# print("copy list: ",l1)
# l1.append(2)
# x = l1.count(2) # it will count howmany given elements are present in a list 
# print("count of 2 in list: ",x)
# # l1.extend(1,2,3)
# # print("extend list: ",l1)
# l1.extend(l2) #Add the elements of a list (or any iterable), to the end of the current list.
# print("extend list: ",l1)
# x = l1.index(3) #What is the position of the value 3, [0]=1, [1]=2, [2]=3.
# print("index of val 3: ",x)
# l1.pop() #it will pop out the last element here 3 will poped.
# print("pop from list: ",l1)
# l1.remove(2) #it will remove the given element from the list
# print("remove from list: ",l1)
# l2.reverse() #it will revers the entire list.
# print("reverse a list: ",l2)
# l1.sort() #it will sort the list l1.
# print("sort a list: ",l1)

# print("----------Tuple---------------")
# #Python has two built-in methods that we can use on tuples. count,index, Becuse its a Immutable.
# t1 = (1,2,2,3,4,5,6)
# print("print a Tuple: ",t1)
# x = t1.count(2) # it will count howmany given elements are present in a Tuple, here 2 has 2Nos. 
# print("count val in a Tuple: ",x)
# x= t1.index(3) #What is the position of the value 3, [0]=1, [1]=2, [2]=2, [3]=3.
# print("print index val from Tuple: ",x)

print("----------Dictionary---------------")
d = {1:"Vinayak", 2:"Vishal", 3:"Suhas", 4:"Pramod"}
d1 = {1:"Vinz", 2:"Vish", 3:"Suhu", 4:"Prom"}

# d.clear() #it will Removes all the elements from the dictionary
# print("clear the Dictionary: ",d)

# d = d1.copy() # it will Returns a copy of the dictionary d1 to d.
# print("copy the Dictionary d1 to d: ",d)

# x = d.get(1) # it will Returns the value of the specified key i,e,. 1:"vinz"
# print("getting the specifide kye value from Dictionary: ",x)

# x = (1,2,3)
# y= 'v'
# z = dict.fromkeys(x,y) #it will Returns a dictionary with the specified keys and value 
# print(z)               #i,e,. 1:'v', 2:v', 3:'v'.

# x = d.items() # It will Returns a list containing a tuple for each key value pair 
# print(x)      #i,e,. dict_items([(1, 'Vinz'), (2, 'Vish'), (3, 'Suhu'), (4, 'Prom')])

# x = d.keys() # it will Returns a list containing the dictionary's keys
# print(x)     # i,e,. dict_keys([1, 2, 3, 4])

# x = d.values() # it will Returns a list containing the dictionary's values.
# print(x)     # i,e,. dict_values(['Vinz', 'Vish', 'Suhu', 'Prom'])

# x = d.pop(1) # it will Removes the element with the specified key i,e,. 1:vinz
# print(x)

# x = d.popitem() # it will Removes the last item i,e,. (4:'Prom')
# print(x)

# print(len(d))
# d.update({3:'vinayak'}) #it will Updates the dictionary with the specified key-value pairs
# print(d)

# d.setdefault(2,'pramod') #	Returns the value of the specified key. 
# print(d)                  #If the key does not exist: insert the key, with the specified value)

for i,j in dict.items(d1):
    print(i,j)

# for i,j in dict.keys(d1):
#     print(i)

# for i,j in dict.values(d1):
#     print(j)

print("----------Strings---------------")



