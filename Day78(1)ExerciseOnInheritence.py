# 🔧 Requirements:
# 1. Base Class: Person
# Attributes:

# name (string)

# age (int)

# Method:

# introduce() → prints:
# "Hi, I'm {name} and I'm {age} years old."

# 2. Derived Class: Student
# Inherits from Person

# Additional Attributes:

# student_id (string)

# grades (list of numbers)

# Methods:

# get_average() → returns average of grades

# Override introduce() to say:
# "Hi, I'm student {name}, ID: {student_id}, and I'm {age} years old."

# 3. Derived Class: Teacher
# Inherits from Person

# Additional Attributes:

# employee_id (string)

# subject (string)

# Override introduce() to say:
# "Hello, I'm Professor {name}, I teach {subject}."

# Add input validation (age > 0, grades between 0–100).

# Add a method in Person like is_adult() returning True if age >= 18.


class Person:
    def __init__(self,name: str,age: int):
        self.name = name
        if(age>0):
         self.age = age
        else:
            raise Exception("Age cannot be negative")

    def introduce(self):
        print(f"Hi, I\'m {self.name} and I\'m {self.age} years old.")

    def is_adult(self):
        return self.age >=18    


class Student(Person):
    def __init__(self, name: str, age: int,student_id : str,grades: list[int]):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = [] 
        for grade in grades:
            if(grade>=0 and grade<=100):
               self.grades.append(grade)
            else:
                raise Exception("Grades should be between 0-100") 

    def get_average(self):
        return sum(self.grades)/len(self.grades)
    
    def introduce(self):
        print(f"Hi, I\'m student {self.name}, ID: {self.student_id}, and I'm {self.age} years old.")

class Teacher(Person):
    def __init__(self, name: str, age: int,employee_id: str,subject: str):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def introduce(self):
        print(f"Hello, I\'m Professor {self.name}, I teach {self.subject}.")



people = [
    Student("Alice", 20, "S123", [85, 90, 78]),
    Teacher("Dr. Smith", 45, "T987", "Physics"),
    Student("Bob", 22, "S456", [70, 80, 88]),
]

for person in people:
    person.introduce()
    if isinstance(person, Student):
        print("Average Grade:", person.get_average())
    print()
        
