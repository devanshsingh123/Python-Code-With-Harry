

class Employee:
    def __init__(self,name):
        self.__name  = name



obj = Employee("Devansh")
#print(obj.__name) # This will give error

print(obj._Employee__name) # This way it can be accessed indirectly , This is known as Name Mangling

print(obj.__dir__())