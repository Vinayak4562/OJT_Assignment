# SCOPE

a = 10   # Global variable
b = 10   # Global variable

# def sum():
#     a = 1     #Local Variable
#     b = 2     #Local Variable
#     c = a + b
#     print(c)

# d = a + b
# print(d)

# sum()

# # we can access global variable locally by using globale keyword.
# print("we can access global variable locally by using globale keyword")
# def sum():
#     global a
#     a = 1   #Local Variable
#     b = 2     #Local Variable
#     print(a)
#     c = a + b
#     print(c)

# print(a)
# sum()

# we can access global variable locally by using globals keyword, it will give access to all
# global variable.
print("we can access global variable locally by using globals keyword")
def sum():
    x = globals()['a']
    a = 1   #Local Variable
    b = 2     #Local Variable
    print(a)
    c = x + b  # 10+2 = 12
    print(c)
    # globals()['a'] = 111
    
print(a)
sum()