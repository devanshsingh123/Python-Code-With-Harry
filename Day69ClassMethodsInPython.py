class Employee:
    # Class variable
    company = "Google"

    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def changeCompany(self, newCompany):
        self.company = newCompany

e1 = Employee("John", 1000)
e1.changeCompany("Microsoft")
print(e1.company)  # Output: Microsoft        