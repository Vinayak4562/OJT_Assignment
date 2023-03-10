list = ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']     # create the list
list1 = []
for i in list:                                                  # To iterate a list
    if i[0].islower():                                          # to chek the word statrs from lower case or not
        list1.append(i)                                         # if its lowercase append it in to list1
print("The words starting with lowercase letter are:", list1)   # to print the list1
 

# # extract the words starting with lowercase letter using a list comprehension

# list = ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']     # create the list

# result = [i for i in list if i[0].islower()]            # extract the words starting with lowercase letter using a list comprehension

# print("The words starting with lowercase letter are:", result)  # print the result
