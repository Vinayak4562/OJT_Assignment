# formal Arguments and Actchual Arguments
# there are 4 types of Actchual Arguments.
# 1.Positional Arguments
# 2.Keyword Arguments
# 3.Default Arguments
# 4.Variable Arguments
# Keyword Variable length Arguments--->[(*arg) and(**kwarg)].

# 1.Positional Arguments
print("1.Positional Arguments")

def stu1(name,age):
    print(name)
    print(age)

stu1("vinay",28)

# 2.Keyword Arguments
print("2.Keyword Arguments")

def stu2(name,age):
    print(name)
    print(age)

stu2(age=28, name="vinay")

# 3.Default Arguments
print("3.Default Arguments")

def stu2(name,age=28):
    print(name)
    print(age)

stu2("vinay")
stu2("vinay",29)

# 4.Variable Arguments
print("4.Variable Arguments")

def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)

sum(1,2,3,4,5)

# Keyword Variable length Arguments
print("Keyword Variable length Arguments")

# def persion(name, *data):  # Here it will take as Tuple (*arg)
#     print(name)
#     print(data)

# persion("vinayak",28,"Bangalore", 9739223665)

def persion(name, **data):  # Here it will take as Dictinory (**kwarg)
    print(name)
    print(data)

persion("vinayak", age=28,city="Bangalore", Mobile=9739223665)


print("------------------------------------")

def persion(name, **data):  # Here it will take as Dictinory as key and value pairs.
    print(name)
    
    for i,j in data.items():
        print(i,"--",j)

persion("vinayak", age=28,city="Bangalore", Mobile=9739223665)