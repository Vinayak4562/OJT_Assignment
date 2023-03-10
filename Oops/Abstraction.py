# abstraction is used to hiding the implimentation.
# Abstract method: the method with the decleration not with deffenition.
# Abstract Class: the class which contain Abstract methods.
# To create Abstract Class we have to import Abstract Base Class module.

from abc import ABC,abstractmethod

class Abstact_Class(ABC):     # Abstract Class
    @abstractmethod           #To make abstract Method we should use decorator
    def display(self):
        None

    @abstractmethod
    def show(self):
        None

class Aclass(Abstact_Class):     # Abstract Class cz its only consists one method.
    def display(self):
        print("display method in Abstact class")


class Concrete_class(Abstact_Class):    # Concreet Class cz its contains all the methods.
    def display(self):
        print("Display method in Concrete Class")

    def show(self):
        print("show method in Concrete Class")


# obj1 = Abstact_Class() #TypeError: Can't instantiate abstract class Abstact_Class with abstract methods display, show
# obj2 = Aclass() #TypeError: Can't instantiate abstract class Abstact_Class with abstract methods display, show
obj3 = Concrete_class()
obj3.display()
obj3.show()