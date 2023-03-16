
dict1 = {'name': 'Msys', 'Place': 'Pune'}                   # Creating the dictionarie dict1
dict2 = {'EmpID': 1, 'Salary': 50000}                       # Creating the dictionarie dict2

dict_merged = {**dict1, **dict2}                            # Merging the dictionaries into a single dictionary

dict_merged['Salary'] = dict_merged['Salary'] * 1.1         # Updating the salary by 10%

dict_merged['Age'] = 35                                     # Updating the age to 35 (assuming the age is not in any of the dictionaries)
print("Dictionarie after updating:",dict_merged)

values_tuple = tuple(dict_merged.values())                  # Extracting and printing all the values in tuple
keys_tuple = tuple(dict_merged.keys())                      # Extracting and printing all the keys in tuple
print("Values tuple:", values_tuple)
print("Keys tuple:", keys_tuple)

del dict_merged['Age']                                      # Deleting the element with key 'Age' and printing the dictionary elements
print("Merged dictionary after deleting 'Age' element:", dict_merged)
