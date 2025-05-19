# 💼 Exercise: Employees and Pay Calculation
# You are designing a payroll system for a company. There is a base class Employee and two subclasses: FullTimeEmployee and PartTimeEmployee.

# 🧩 Requirements:
# Employee should have:

# Attributes: name and base_salary

# Method: calculate_pay() — just return base_salary

# FullTimeEmployee should:

# Inherit from Employee

# Override calculate_pay() to return base_salary + 20% bonus

# PartTimeEmployee should:

# Inherit from Employee

# Override calculate_pay() to return base_salary - 10% tax

# All classes should have a __str__() method to print the employee type and pay.


class Employee:
    def __init__(self,name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self) -> float:
        return self.base_salary
    
class FullTimeEmployee(Employee):
    def calculate_pay(self) -> float:
        return self.base_salary + (0.2 * self.base_salary)

    def __str__(self) -> str:
        return f"FullTimeEmployee: {self.name}, Pay: ₹{self.calculate_pay()}"   
    

class PartTimeEmployee(Employee):
    def calculate_pay(self) -> float:
        return self.base_salary - (0.1 * self.base_salary)

    def __str__(self) -> str:
        return f"PartTimeEmployee: {self.name}, Pay: ₹{self.calculate_pay()}"
   
