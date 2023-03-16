f = lambda x, y: y**2 if x > y else x**2



x_is_greater = f(5,2)      #If x is greater than y then it should return square of y i,e,. 2x2=4
print("x is greater than y so it returning y square: ",x_is_greater)

y_is_greater = f(4,8)      #if y is greater than x, then it should return square of x i,e,. 4x4=16
print("y is greater than x so it returning x square: ",y_is_greater)