def get_hypotenuse(side1, side2):
    hypotenuse = (side1**2 + side2**2)*0.5
    result = "{:.2f}".format(hypotenuse)   # To ristrict the 2 decimal points
    return result

side1 = int(input("Enter the value os side 1: "))
side2 = int(input("Enter the value os side 2: "))

print(f'hypotenuse is {get_hypotenuse(side1,side2)}')

# def get_hypotenuse(side1):
#     hypotenuse = (side1[0]**2 + side1[1]**2)*0.5
#     result = "{:.2f}".format(hypotenuse)   # To ristrict the 2 decimal points
#     return result

# side1 = tuple(map(int,(input().split())))
# print(get_hypotenuse(side1))


# x = list(map(int,(input().split())))
# print(x)