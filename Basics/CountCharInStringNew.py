# string = "Vinayak havannavar"
string = input("Enter a string: ")                    # Prompt the user to enter a string
print("You entered: ", string)                        # Print the user's input which user was entered.

count = 0                                             # used to store the num of char.
char_count = {}                                       # used this empty dictionary to store the char count char is key num as values.         
for char in string:                                   #  this loop will run till reaches last index.    
    if char.isalpha() or char.isdigit():              # Check if the character is alphabetic
        count += 1                                    # increment the count
        if char in char_count:                        # if char is exist in the dict key.
            char_count[char] += 1                     # increment the count.
        else:
            char_count[char] = 1                      # dont exist in dictionary add it in to dictionary.

            
print("Total Num Of Char: ",count)
print("Character count:")
for char, count in char_count.items():                 # to acess the key and value pairs
    print(f"{char} --> {count},", end="  ")            # to print key and value pairs