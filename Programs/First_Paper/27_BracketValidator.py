class BracketValidator:                                         #Class for validating brackets in a string
    def __init__(self):
        self.stack = []

    def is_valid(self, s):                                  #Checks if the string has valid bracket ordering 
      
        bracket_map = {')': '(', '}': '{', ']': '['}        # Create a dictionary to map opening brackets to closing bracket
        
        for char in s:                                      # Iterate through each character in the string            
            if char in bracket_map.values():                # If the character is an opening bracket, add it to the stack
                self.stack.append(char)            
            elif char in bracket_map.keys():                # If the character is a closing bracket, check if it matches the last opening bracket on the stack                
                if not self.stack:                          # If there are no opening brackets on the stack, the string is invalid
                    return f'Invalid Brackets'
                
                elif bracket_map[char] != self.stack.pop():   # If the closing bracket does not match the corresponding opening bracket, the string is invalid
                    return f'Invalid Brackets'                # If the character is not a bracket, ignore it
            

        
        if self.stack:                           # If there are any opening brackets left on the stack, the string is invalid
            return f'Invalid Brackets'        
        return f'Valid Brackets'                             # If we make it through the string without finding any issues, the string is valid


validator = BracketValidator()

print(validator.is_valid("()[]{}"))             #Valid Brackets 
print(validator.is_valid("[)"))                #Invalid Brackets

