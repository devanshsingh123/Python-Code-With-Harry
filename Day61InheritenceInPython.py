

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f'The engine of {self.brand} {self.model} is starting...')

    

class Car(Vehicle):
    def __init__(self,brand,model,year,num_doors):
        super().__init__(brand,model,year)
        self.num_doors = num_doors

    def describe(self):
        print(f'This car is a {self.year} {self.brand} {self.model} with {self.num_doors} doors.')


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year,type):
        super().__init__(brand, model, year)
        self.type = type

    
    def describe(self):
        print(f'This motorcycle is a {self.type} {self.brand} {self.model} from {self.year}.')


try:  
    i1 = Car('BMW','3 Series',2019,4) 
    i1.start_engine() 
    i1.describe()

    i2 = Motorcycle('TRIUMPH','Scrambler 400 X',2020,'Bonneville') 
    i2.start_engine()
    i2.describe()
except  Exception as err:
    print(err)

