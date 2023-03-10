#Conditional/Branching statment: these are the statements which will check for the condion
# if condition get satisifid it will execute some block of statements.
# if condition not get satisifid it will execute another block of statements.
# there are 5 conditional statements 
# if, if-else, if-else-if, nested if , if-ladder
# IF-Condiion
print("---------IF Condiion----------")
n = 10
if n == 10:
    print("aila its TEN")
    n+=1


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  

# IF- ELSE Condiion
print("---------IF- ELSE Condiion----------")
n = 11
if n == 10:
    print("aila its TEN")
    n+=1
else:
    print("aila its not TEN")


 # IF- ELSE - IF Condiion
print("---------IF- ELSE - IF Condiion----------")
n = 1
if n == 10:
    print("aila its TEN")
elif n== 11:
    print("aila its not Eleven")
else:
    print("Neither is 10 nor 11")


# Nested IF Condiion
print("---------Nested IF Condiion----------")
x = 2
y = 20
if x > 10:
    print("Greater than ten,")
    if x < 10:
        print("Less than ten,")
    else:
        print("x is equal to ten,")

