# names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']
# sorted_names = sorted(names_list)
# print(sorted_names)


names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

last_char = lambda x: x[-1]                         # Define a lambda function to extract the last character of a string

sorted_names = sorted(names_list, key=last_char)    # Sort the names list using the last character of each word

print(sorted_names)                                 # Print the sorted list

