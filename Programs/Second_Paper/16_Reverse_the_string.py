def reverse_words(string):
    words = string.split()                          # split the string into words

    reversed_words = words[::-1]                    # reverse the order of the words
    
    reversed_string = " ".join(reversed_words)      # join the reversed words back into a string

    return reversed_string                          # Return the final output string

input_string = "Hello World"
output_string = reverse_words(input_string)
print(output_string)                                # Output: "World Hello"