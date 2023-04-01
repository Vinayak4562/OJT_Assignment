# input = input("Enter the number: ")         # To take a user input  
# output =""                                  # to print the output
# count = 0                                   # count cvariable used to digits
# for i in input:                             # To iterate the input string
#     if i not in output:                     # If the digit is not present in the output it will execute the if statement
#         output += i                         # increment the output by i
#         count += int(i)                     # converting the string in to digit and add it to the count
# print(output)
# print(count)


input = "12113421"
output = ''.join(set(input))
count = sum(int(i) for i in output)
print(output)
print(count)
