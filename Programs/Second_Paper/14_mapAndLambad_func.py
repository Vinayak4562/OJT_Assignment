
list_1 = ['Msys', 'Tata', 'Wells', 'Mobinius']      # Defining the first list

list_2 = ['Technologies', 'Power', 'Fargo', 'Technologies'] # Defining the second list

my_list = list(map(lambda x, y: x + '-' + y, list_1, list_2)) # Apply the map function with a lambda function that concatenates 2 I/P

print(my_list)  # Display the result
