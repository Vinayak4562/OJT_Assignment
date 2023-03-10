
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Starting engine...")
    
class Car(Vehicle):
    def __init__(self,num_doors):
        self.num_doors = num_doors
    
    def drive(self):
        print("Driving the car throug Petrol...")
    
class ElectricCar(Car):
    def __init__(self, range_per_charge):
        self.range_per_charge = range_per_charge
    
    def charge(self):
        print("Driving the car throug battery...")



obj = ElectricCar("100 Km")
obj.start_engine()
obj.drive()
obj.charge()

