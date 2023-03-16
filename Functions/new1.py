# class Test:
#     def add(self,a,b):
#         return a+b
    
#     def sub(self,a,b):
#         return a-b

# a= Test()
# # print(a.add(2,4))

# def mul(self,a,b):
#     return a*b

# Test.sub= mul

# print(a.add(2,4))
# print(a.sub(4,2))

class Monkey:
    def func1(self):
        print("this is before monkey paching...")

    
a = Monkey()
a.func1()

def func2():
    print("this is out of class....")
print(func2())

