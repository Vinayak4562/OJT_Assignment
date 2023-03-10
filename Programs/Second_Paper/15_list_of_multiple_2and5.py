
list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]      # Defining the input list


result_list = list(filter(lambda x: x % 2 == 0 or x % 5 == 0, list_1))    # Use the filter() function with a lambda function to filter the 
print(result_list)                                                        #list of numbers that are multiples of either 2 or 5


