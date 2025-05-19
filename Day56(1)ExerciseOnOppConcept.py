# ✅ 1. Class & Object Creation
# 📌 Problem:
# Create a class Person with attributes name and age. Then, create an object of this class and display its details.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# ✅ 2. Encapsulation (Private Attributes)
# 📌 Problem:
# Create a class BankAccount with a private attribute __balance. Add methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self,balance: int = 0):
        self.__balance = balance

    def deposit(self,amount: int):
        self.__balance += amount

    def withdraw(self,amount: int):
        self.__balance -= amount

    def get_balance(self) -> None:
        print(f"Current Balance: {self.__balance}")


# acc = BankAccount(1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.get_balance()     


# 🧪 Exercise: Create a Student Class with Validation
# 🎯 Requirements:
# Create a Student class with the following:

# Attributes: name, age, grades (list of integers)

# Implement a @staticmethod called is_valid_grade():

# It should check if a given grade is a number between 0 and 100 (inclusive)

# In the __init__ method:

# Use the static method to validate each grade in the list

# If any grade is invalid, raise a ValueError

# Add a method get_average() that returns the student's average grade.



class Student:   
        @staticmethod
        def is_valid_grade(grade):
            if(grade > 100 or grade < 0):
                return False
            else:
                return True
            
        def __init__(self,name,age,grades :list[int]):
            self.name = name
            self.age = age
            self.grades = []
            for  grade in grades:
                if(self.is_valid_grade(grade)):
                    self.grades.append(grade)
                else:
                    raise ValueError("Grades should be between 1 and 0")
                
        def get_average(self):
            return sum(self.grades)/(len(self.grades))
 
                
    

# Expected behavior:
# student = Student("Alice", 18, [85, 90, 78])
# print(student.get_average())


# # Invalid case:
# bad_student = Student("Bob", 19, [101, 90])


# 🧪 Exercise #2: Employee Class with Static Validation
# 🎯 Requirements:
# Create an Employee class with the following:

# 🔹 Attributes:
# name (string)

# position (string)

# salary (float)

# 🔹 Static Method:
# @staticmethod def is_valid_salary(salary)
# → Returns True if salary is a positive number (greater than 0), else False

# 🔹 In __init__:
# Validate the salary using the static method

# Raise a ValueError if it’s invalid

# 🔹 Instance Method:
# apply_raise(percent)
# → Increases the salary by the given percentage
# (e.g., 10% raise means salary becomes salary * 1.10)


class Employee:
    @staticmethod
    def is_valid_salary(salary):
        return True if salary > 0 else False
    
    def __init__(self,name :str,position :str,salary :float):
        self.name = name
        self.position = position
        if(self.is_valid_salary(salary)):
            self.salary = salary
        else:
            raise ValueError("Salary should not be less than 0")
    
    def apply_raise(self,percent):
        self.salary *= (1+(percent/100))


# try:
#     emp = Employee("John Doe", "Developer", 50000)
#     print(emp.salary)  # 50000

#     emp.apply_raise(10)
#     print(emp.salary)  # 55000.0

#     emp2 = Employee("Jane Smith", "Designer", -3000)  # Should raise ValueError
# except ValueError as err:
#     print(err)


# 💼 Advanced Challenge: Product Management System
# 🛒 Problem Statement:
# You are building a basic inventory system for a store. Create a Product class with the following features:

# 🔹 Attributes:
# name (string)

# category (string)

# price (float)

# stock_quantity (int)

# 🔹 Static Method:
# @staticmethod def is_valid_price(price)
# → Return True if price > 0, else False

# @staticmethod def is_valid_stock(stock)
# → Return True if stock is an integer ≥ 0, else False

# 🔹 Validation in __init__:
# Use the static methods to validate price and stock_quantity

# Raise ValueError if any are invalid

# 🔹 Instance Methods:
# apply_discount(percent)
# → Reduces the price by a percentage
# (e.g. 20% discount on $100 → price becomes $80)

# purchase(quantity)
# → Deducts the quantity from stock_quantity
# → If not enough stock, raise an exception: "Insufficient stock."

# restock(quantity)
# → Increases the stock_quantity by the given amount
# → Only accepts positive integers


class Product:

    @staticmethod
    def is_valid_price(price):
        return price > 0
    
    @staticmethod
    def is_valid_stock(stock):
        return stock >= 0
    
    
    def __init__(self,name: str, category: str,price: float,stock_quantity: int):
        self.name = name
        self.category = category
        if(self.is_valid_price(price)):
            self.price = price
        else:
            raise ValueError("Price can not be negative or Zero!")
        
        if(self.is_valid_stock(stock_quantity)):
            self.stock_quantity = stock_quantity
        else:
            raise ValueError("Stock Quantity cannot be negative")
        
    def apply_discount(self,percent):
        self.price -= (percent/100)*self.price

    def purchase(self,quantity):
        if(self.stock_quantity < quantity):
            raise Exception("Insufficient Stock!")
        else:
            self.stock_quantity-=quantity
    
    def restock(self,quantity):
        if(quantity<0):
            raise ValueError("In restock the added quantity cannot be negative!")
        else:
            self.stock_quantity += quantity

try:
    item = Product("Wireless Mouse", "Electronics", 1500.0, 10)
    item.apply_discount(10)
    print(item.price)  # 1350.0

    item.purchase(3)
    print(item.stock_quantity)  # 7

    item.restock(5)
    print(item.stock_quantity)  # 12

    bad_item = Product("Fake Watch", "Fashion", -500, 5)  # Should raise ValueError
except  Exception as err :
    print(err)

    