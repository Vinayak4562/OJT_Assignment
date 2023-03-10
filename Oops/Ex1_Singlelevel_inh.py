class Animal:
    def __init__(self, name):
        self.name = name
    
       
class Dog(Animal):
    def speak(self):
        print("Bow Bow")

my_dog = Dog("Rocky")
print(my_dog.name)
my_dog.speak()
