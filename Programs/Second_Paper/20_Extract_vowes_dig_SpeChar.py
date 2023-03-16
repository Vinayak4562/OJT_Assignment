def extract_digits(string):         #Function to extract digits and return them in sorted order
    digits = [char for char in string if char.isdigit()]
    digits = sorted(set(digits))
    return "".join(digits)

def extract_special_chars(string):   #Function to extract special characters
    special_chars = [char for char in string if not char.isalnum()]
    return "".join(special_chars)

def extract_vowels(string):         #Function to extract vowels in reverse orde
    vowels = [char for char in string if char.lower() in "aeiou"]
    vowels.reverse()
    return "".join(vowels)


input_string = "abcd123bye09@8"

digits = extract_digits(input_string)
print("Digits:", digits)

special_chars = extract_special_chars(input_string)
print("Special characters:", special_chars)

vowels = extract_vowels(input_string)
print("Vowels:", vowels)

# Out Put:
# Digits: 012389
# Special characters: @
# Vowels: ea
