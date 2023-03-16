num = int(input("Enter a number: "))                    # takeing user input

reverse_num = 0                                         # initialize reverse_num variable

while num > 0:
    digit = num % 10                                     # get the rightmost digit (last Digit)
    reverse_num = (reverse_num * 10) + digit             # append the digit to reverse_num
    num //= 10                                           # remove the rightmost (last Digit) digit from num

print("The reverse of the number is:", reverse_num)      # print the result