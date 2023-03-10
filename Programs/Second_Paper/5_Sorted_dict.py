
dictionary = {'Msys Technologies': 'Sanjay Sehgal', 'Infosys': 'Salil Parekh', 'TCS': 'Rajesh Gopinathan', 'Wipro': 'Thierry Delaporte'}# Given dictionary


values_list = list(dictionary.values())                 # to get the values from dictionary n stored in values list
sorted_values = sorted(values_list)                     # to sort the values in alphabetical order.

Key_list = list(dictionary.keys())
sorted_keys = sorted(Key_list)
print("The sorted list of values is:", sorted_values)   # print the sorted list of values
print()
print("The sorted list of Keys is:", sorted_keys)   # print the sorted list of values
print()
dic = sorted(dictionary)
print("The sorted dictionary :",dic )   # print the sorted list of values

