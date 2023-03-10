#Implimenting the same thing in different ways
# we can acchive the Polymorphism using two methods 
# 1.Method Over-loading and 2.Method Over-riding
# in Method Over-loading :- oprator overloading and Method Over-loading
# oprator overloading (+): Ex Concatination and Addition its behave deppending on type of data.
# Method Over-loading ; we can achive by providing default Arguments.
## Method name should be same. Arguments should be Differant.

print("Method Over-loading")
a = "Vinayak"
b = " Havannavar"
print(a + b)
c = 10
d = 20
print(c + d)

print("========================================================")

class Moverloading:
    def display(self, a = None, b = None ):
        print(a,b)

obj = Moverloading()
obj.display()
obj.display(10)
obj.display(10,20)

print("========================================================")

print("Method Over-riding")
class Father:
    def transportation(self):
        print("Cycle is a transportation medium")

class Son(Father):
    def transportation(self):
        print("Bike is a transportation medium")

obj1 = Father()
obj2 = Son()
obj1.transportation()
obj2.transportation()

print("========================================================")

