my_string = 'MsYs TecHNOlogiEs iS a gREat place To woRk'   # Define the string


lower_count = 0                                             # Initialize counters for lowercase 
upper_count = 0                                             # Initialize counters for uppercase letters

for char in my_string:                                      #  to Iterate through the string and update the counters.
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1
        
print(f"Number of uppercase letters: {upper_count}")            # Number of uppercase letters: 13
print(f"Number of lowercase letters: {lower_count}")            # Number of lowercase letters: 20




