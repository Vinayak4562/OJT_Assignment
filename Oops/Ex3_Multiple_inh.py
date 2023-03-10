class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Starting engine...")
    
class car:
    def __init__(self,battery):
        self.battery=battery

    def elecric_car(self):
        print("Running on Battery...")
    
class Elecric_bus(Vehicle, car):
    
    def drive(self):
        print("Driving the Electric Bus...")

obj =Elecric_bus ("TATA", "Tata-2023",2023)
obj.start_engine()   # Output: Starting engine...
obj.elecric_car()   # Output: Flying...
obj.drive()   # Output: Driving the amphibious vehicle...
