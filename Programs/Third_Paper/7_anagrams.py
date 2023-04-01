""" Anagram = An Anagram is a word or phrase that is formed by rearranging all the letters of a different word 
or phrase exactly once such as elbow and below."""

def is_anagram(string1, string2):
   
    string1 = string1.replace(" ", "").lower()              # Remove any spaces and convert the strings to lowercase
    string2 = string2.replace(" ", "").lower()              # Remove any spaces and convert the strings to lowercase
    
   
    if len(string1) != len(string2):                       # Check if the lengths of the strings are the same
        return False                                       # its deffent simply returnig False here    
    
    empt_dict = {}                                    # Create a empty dictionary to store the frequency of characters in string1
    for char in string1:
        empt_dict[char] = empt_dict.get(char, 0) + 1    
    
    for char in string2:                  # Check if the characters in string2 are present in the dictionary and have the same dict
        if char not in empt_dict:
            return False
        empt_dict[char] -= 1
        if empt_dict[char] < 0:
            return False
    
    return True


print(is_anagram("elbow", "below"))                 # True
print(is_anagram("hello", "world"))                 # False

