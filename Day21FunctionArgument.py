# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

# # 1. Required Arguments
# def greet(name):
#     print(f"Hello {name}!")

# # This will work
# greet("John")  
# # This will raise an error if argument is not provided
# # greet()  

# # 2. Default Arguments
# def greet_with_default(name="Guest"):
#     print(f"Hello {name}!")

# greet_with_default()  # Uses default value "Guest"
# greet_with_default("Alice")  # Uses provided value "Alice"

# # 3. Keyword Arguments
# def student_info(name, age, course):
#     print(f"Name: {name}, Age: {age}, Course: {course}")

# # Arguments can be provided in any order using keywords
# student_info(age=20, course="Python", name="Bob")
# student_info(name="Charlie", course="Java", age=25)

# # 4. Variable Length Arguments
# # *args (Tuple)
# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_numbers(1, 2, 3, 4, 5))  # Can take any number of arguments

# # **kwargs (Dictionary)
# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name="David", job="Developer", country="USA")

# # Combining Different Types of Arguments
# def mixed_arguments(required, *args, default="Default", **kwargs):
#     print(f"Required: {required}")
#     print(f"Args: {args}")
#     print(f"Default: {default}")
#     print(f"Kwargs: {kwargs}")

# mixed_arguments("Must", 1, 2, 3, default="Changed", x=10, y=20)

# Required Arguments

def checkAgeStatus(age):
    if(age > 18):
        print("Age status checked and passed !")
    else:
        print("Age status checked and failed !")

# Here the argument is Required

#checkAgeStatus(13)

# This below will throw error

#checkAgeStatus()


# Default Arguments
# The order of using defualt parameters can only be done at the end if used with required parameter
# Below function uves error becuase of incorrect order

# def checkStaus_default(name="Not shared",age,Org = "Not shared"):

# Correct form

# def checkStaus_default(age,name="Not shared",Org = "Not shared"):
#     if(age>18):
#         print("Age Status approved ! Info: Name: ",name,",Org: ",Org,",Age: ",age)
#     else:
#         print("Age Status Rejected ! Info: Name: ",name,",Org: ",Org,",Age: ",age)


# checkStaus_default(21)
# checkStaus_default(22,name="Devansh",Org="Accenture")
# checkStaus_default(22,name="Devansh",Org="Accenture")
#checkStaus_default(22,Name="Devansh",org="Accenture") # Error


# Variable length Arguments
# Here i will be checkin the Variable lenth argument

# def name_List(*names):
#     for name in names:
#         print(name)


# name_List("Devansh","Aman","Raj","Ravi")

# As a dictionary if i am taking arguments 

def using_Object(**obj):
    # name , age , infojson = obj.values()
    name , infoJson , *Others = obj.values()
    print(name,Others,infoJson)

using_Object(name = "Devansh",age = 21,infoJson = {
    "data1" :"value1",
    "data2" : "Value2",
    "data3" : "value3"
})    







