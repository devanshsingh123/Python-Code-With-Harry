# Lambda Functions in Python
# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda arguments: expression


# normal function

# def double(x):
#     return x*2

# print(double(5))

# Lamda Function

double = lambda x: x*2

print(double(2))

value = lambda x,y: (x*y)/(x+y)

print(value(4,6))

seen = lambda x,y:print(f"This is printed through lamda function and x:{x} and y:{y} and (x+y)/(x*y) : {(x+y)/(x*y)}")

seen(4,8)


