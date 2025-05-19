
class student:
    def __init__(self, name, roll_number, standard, emergency_contact):
        self.name = name
        self.roll_number = roll_number
        self.standard = standard
        self.emergency_contact = emergency_contact
    
    def info(self):
        print(f"name : {self.name} \nRoll Number: {self.roll_number}\nClass: {self.standard}\nContact: {self.emergency_contact}")

class Car:

    ''' This class is about cars with data attributes brand,model,year and 
        have a function name start_engine'''

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f'{self.brand} engine started!')



s1 = student("Devansh","12Fhjy","X","987679079")
s2 = student("RAVI","13Fhjy","X","987679045")
s3 = student("DAVID","14Fhjy","X","987679034")
s4 = student("SHYAM","15Fhjy","X","987679078")


s1.info()
s2.info()
s3.info()
s4.info()