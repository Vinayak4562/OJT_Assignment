
def replace_duplicates(string):
   
    modified_string = ""                                         # Initialize an empty string to store the modified string

    i = 0                                                       # Iterate through the characters in the string
    while i < len(string):
        
        modified_string += string[i]                            # Append the current character to the modified string
        
        if i+1 < len(string) and string[i] == string[i+1]:      # Check if the current character is equal to the next character
            
            modified_string += '_'                              # If so, append '_' to the modified string            
            i += 1                                              # Skip the next character        
        i += 1                                                  # Increment the index variable   
    return modified_string                                      # Return the modified string

input_string = 'abcdaa hssbbye'
output_string = replace_duplicates(input_string)
print(output_string)                                            # Output: 'abcda_ hs_b_ye'

