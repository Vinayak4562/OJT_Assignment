a = 2
b = 4
# print ("a=",a, " ", "b =" ,b)
# # 1) Airthmetic operator
# print(" ---------1) Airthmetic operator-----------")
# # adition 
# c = a + b
# print("Addition of a and b is = ",c)

# # substaction 
# c = b - a
# print("substaction of a and b is = ",c)

# # Mulriplication
# c = a * b
# print("Mulriplication of a and b is = ",c) 

# # Devision
# c = a / b
# print("Devision of a and b is = ",c) 

# # Floordevision
# c = a // b
# print("Floordevision of a and b is = ",c) 

# # modulus
# c = a % b
# print("modulus of a and b is = ",c) 

# # Exponential
# c = a ** b
# print("Exponential of a and b is = ",c)

# # 2) Relational operator it will give boolean ourput
# print("------------2) Relational operator------------")
# # Less than operator
# d = a < b
# print(d)

# # Greater than operator
# d = a > b
# print(d)

# # less than or equal to operator
# d = a <= b
# print(d)

# # Greater than or equal to operator
# d = a >= b
# print(d)

# # Equal to operator
# d = a == b
# print(d)

# # Not-Equal to operator
# d = a != b
# print(d)

# # 3) Logical operator
# print("-------------3) Logical operator------------------")
# # And operator when both the condition is TRUE resulr will be the TRUE
# p = 8
# print(p > 8 and p < 10)

# # Or operator when any one of the condition is TRUE resulr will be the TRUE
# p = 8
# print(p > 8 or p < 10)
# # Not operator its a complement (Nagation) of input 
# p = 8
# print(not(p > 8 or p < 10))

# # 4) Assignment operator
# print("---------4) Assignment operator----------") 
# # Equal to assigning 5 to the variable x.
# x = 5	
# print("Equal=",x)

# # Adding(Incrementing by 2) 2 to the x=5 and Assigning it to x=5+2=7.
# x += 2	
# print("Adding (x=5+2)= ",x)

# # Substacting(Decrementing by 2) 2 to the x=7 and Assigning it to x=7-2=5.
# x -= 2	
# print("Substacting(x=7-2)=",x)

# # Multipling 2 to the x=5 and Assigning it to x=5*2=10.
# x *= 2	
# print("Multipling(x=5*2)=",x)

# # Deviding x=10 by 2 and Assigning it to x=10/2=5.0.
# x /= 2	
# print("Deviding(x=10/2)=",x)

# # Doing Floordevision to x=5 by 2 and Assigning it to x=5//2=2.5 ~ 2.0.
# x //= 2	
# print("Floordevision(x=5//2=2.5)=",x)

# # The modulo or mod is the remainder after dividing one number by another num
# # Doing modulus operation to x=2 by 2 and Assigning it to x=2 mod 4=2.
# x %= 4	
# print("modulus(2 mod 4)=",x)

# # Doing exponatial operation to x by 2 and Assigning it to x= 2**2= 4.
# x **= 2	
# print("exponatial(2**2)=",x)

# 5) Bitwise operator: it will operates bit by bit.
print("----------5) Bitwise operator----------")
#AND Operator 	Sets each bit to 1 if both bits are 1
print("Bitwise AND operator = ",6 & 3) #0110 + 0011 = 0010  2

#OR Operator Sets each bit to 1 if one of two bits is 1
print("Bitwise OR operator = ",6 | 3) #0110 + 0011 = 0111  7

#XOR Operator Sets each bit to 1 if only one of two bits is 1
print("Bitwise XOR operator = ",6 ^ 3) #0110 + 0011 = 0101  5 

# NOT Operator Inverts all the bits
print("Bitwise NOT operator = ",~2)  #010 =101
print("Bitwise NOT operator = ",~3)  #011 =100
"""Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
#LeftShift (<<) Operator will Shift left by pushing zeros in from the right and 
# let the leftmost bits fall off.
print("Bitwise LeftShift operator = ",3 << 2) 
#If you push 00 in from the left:3 = 0000000000000011 becomes 12 = 0000000000001100 

#RightShift (>>)Shift right by pushing copies of the leftmost bit in from the left, 
# and let the rightmost bits fall off.
print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010 
 """

# 6) Identity operators is used for comparision 
print("-------6) Identity operators-------------")
# IS operator will 	Returns True if both variables are the same object
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = x
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "=="
              # this comparison returns True because x is equal to y
# ISNOT Operator Returns True if both variables are not the same object
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = x
print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x != y) # to demonstrate the difference betweeen "is not" and "!="
            #this comparison returns False because x is equal to y.

# 7) Membership operators are used to test if a sequence is presented in an object.
print("--------------7) Membership operators-----------")
# IN Operator will Returns True if a sequence with the specified value is present in the object
x = [1, 2, 3, 4]
print(1 in x) # returns True because a sequence with the value 1 is in the list
print(8 in x) # returns False because a sequence with the value 8 is not in the list.

# NOTIN operator will Returns True if a sequence with the specified value is not present in the object
x = [1, 2, 3, 4]
print(8 not in x) # returns True because a sequence with the value 8 is not in the list
print(2 not in x) # returns False because a sequence with the value 2 is Present in the list