# encapsulation can be achieved by using access Specifire, PUBLIC,PROTECTED and PRIVATE.
class Encp_public:
    a = 10
    def display(self):
        print(" I am Public method..")

obj1 = Encp_public()
obj1.display()
print(obj1.a)

print("==============================================")
class Encp_protected:
    _a = 100
    def _display(self):
        print(" i am Protected Method..")

obj2 = Encp_protected()
obj2._display()
print(obj2._a)


print("==============================================")

class Encp_private:
    __a = 1000
    def __display(self):
        print(" i am Private Method..")
        print(self.__a)

obj3 = Encp_private()
obj3.__display()      #Private variables or methods cannot be accessable outside the class
# print(obj3.__a)