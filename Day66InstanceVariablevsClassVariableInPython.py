class Employee:
    companyName = "TechCorp"  # Class variable
    def __init__(self, name):
        self.name = name
        self.raiseAmount = 0.04  # Instance variable

    def showDetails(self):
        print(f"Employee Name: {self.name} and raise amount in {self.companyName} is {self.raiseAmount}")

    
emp1 = Employee("John")
emp1.raiseAmount = 0.05  # Changing instance variable for emp1
emp1.companyName = "Tech Innovations"  # Changing class variable for emp1
emp1.showDetails()  # Output: Employee Name: John
emp2 = Employee("Rohan")
emp2.showDetails()  # Output: Employee Name: Rohan


