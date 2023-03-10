def double (x):
    return 2 * x
print(double(2))


def cube(y):
    return y*y*y
print(cube(2))

# Passing an function an argument to the another function
def own(fx, value):
    return fx(value)
print(own(cube,2))

print("--------------Lambda Function---------------")

double = lambda x: x * 2
print(double(3))

cube = lambda y:y*y*y
print(cube(3))

