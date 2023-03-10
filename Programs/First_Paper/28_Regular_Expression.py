# Regular expressions are allow us to search for general pattern in the Text data.
# re Library allow us to create special pattern strings and then search for    
# matches with text.
import re

data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
reg_exp = r"\s*\([^()]*\)"	# Regular Expression \s is to avoid whitespace .

for string in data:
    result = re.sub(reg_exp, "", string) #re.sub(pattern, repl, string) is used to substitute 
    print(result)   					#occurrences of a pattern in a string with a replacement string.