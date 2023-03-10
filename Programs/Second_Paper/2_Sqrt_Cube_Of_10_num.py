
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # create the list of the first 10 natural numbers
result_sqr = []
result_cube = []                                 # initialize the list to store the squares and cubes

for num in numbers:                         # loop through the numbers list and compute squares and cubes
    if num % 2 == 0:                        # check if the number is even
        square = num ** 2                   # compute the square
        result_sqr.append(square)           # append the square to the result list
    else:                                   # the number is odd
        cube = num ** 3                     # compute the cube
        result_cube.append(cube)                 # append the cube to the result list

print("The Square root of Even Num result list is:", result_sqr)        # print the Square root of Even Num result list
print("The cube root of Odd Num result list is:", result_cube)          # print cube root of Odd Num result list is
