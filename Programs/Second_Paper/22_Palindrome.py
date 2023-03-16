def palindrome_count(text):
   
    words = text.lower().split()         # converting the text in to lower cases and Splitting text into words    
    
    palindromes = {}                    # Initializing an empty dictionary to store the count of palindrome words
    
    for word in words:                  # Looping through each word in the list of words
        
        if word == word[::-1]:          # Checking if the word is a palindrome
           
            if word in palindromes:     # If the word is already in the dictionary, increment its count
                palindromes[word] += 1            
            else:                       # If the word is not in the dictionary, add it with a count of 1
                palindromes[word] = 1    
                   
    return palindromes                   # Returning the dictionary of palindrome words and their count


# Testing the function with the given input
text = "Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331."
print(palindrome_count(text))
