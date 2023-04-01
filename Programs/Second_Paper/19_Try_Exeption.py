def remove_char(string, char):
    if char not in string:
        raise ValueError("Given character is not present in the string. Please try with a new one")
        
    new_string = string.replace(char, "")  # replace all occurrences of the character with an empty string
    return new_string

input_string = input("Enter a string: ")
input_char = input("Enter a character to remove: ")

# try:
output_string = remove_char(input_string, input_char)
print("Result:", output_string)
# except ValueError as e:
#     print(e)
    

# Out Put:
# Enter a string: vinayak
# Enter a character to remove: k
# Result: vinaya

# Enter a string: vinayak
# Enter a character to remove: h
# Given character is not present in the string. Please try with a new one
