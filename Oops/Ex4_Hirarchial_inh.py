class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Starting engine...")
    
class Elec_car(Vehicle):
    def __init__(self,battery):
        self.battery=battery

    def Drive_by(self):
        print("Running on Battery...")
    
class CNG_CAR(Vehicle):
    def __init__(self,CNG):
        self.CNG=CNG
    
    def drive(self):
        print("Running on CNG...")

obj1 = Elec_car ("350 kWh")
obj2 = CNG_CAR("25Ltr")
obj1.start_engine()   
obj2.start_engine()
obj1.Drive_by()
obj2.drive()
