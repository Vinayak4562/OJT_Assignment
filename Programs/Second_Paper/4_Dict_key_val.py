
my_dict = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'Nepal': 'Kathmandu'}

list_keys = list(my_dict.keys())            # Get all the keys in a list
print("Keys: ", list_keys)                  # to print the list of keys

list_values = list(my_dict.values())        # Get all the values in a list
print("Values: ", list_values)              # to print the list of values

key = input("Enter the name of Country: ")  # to take an input from user
value = my_dict.get(key, 'NA')              # Get the value of key in the dictionary
print("Capital city is: " , value)          # to print the value of give Key