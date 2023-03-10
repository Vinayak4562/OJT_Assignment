# def multiply(a, b):                             #This function takes two integer arguments a and b and returns their product.
#     if a == 0 or b == 0:                        # if either a or b is zero the result should returns zero.
#         return 0
#     result = 0                                  #Else result variable is use to store the result of first addition.
#     for i in range(abs(b)):                     # this loop to repeatedly add abs(a) to result abs(b) times. 
#         result += abs(a)
#     if (a < 0 and b > 0) or (a > 0 and b < 0):  # It checks the signs of a and b to determine the sign of the result 
#         return -result                          # and returns the appropriate value.        
#     else:
#         return result

# print(multiply(2,1))     #2
# print(multiply(2,4))     #8
# print(multiply(6,-3 ))   #-18
# print(abs(-84))  


def multiply(a, b):
    result = 0        #taking result as a count
    for i in range(b):    #iterating of b
        result += a    #adding in result one by one a
    return result

print(multiply(-25,4))  
# o/p : 100

