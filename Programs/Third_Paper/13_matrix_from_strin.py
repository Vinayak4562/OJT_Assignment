def matrix_from_string(input_string):
    lines = input_string.strip().split(',')    
    matrix = []
    for line in lines:
        numbers = [float(x) for x in line.strip().split()]
        matrix.append(numbers)
    return matrix

input_string = "3 4 5 , 6 7 8 , 9 10 11 "
print(matrix_from_string(input_string))

# OutPut:[[3.0, 4.0, 5.0], [6.0, 7.0, 8.0], [9.0, 10.0, 11.0]]
