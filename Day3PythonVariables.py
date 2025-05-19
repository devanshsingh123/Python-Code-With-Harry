# # Dynamic Typing

# x = 25

# print(x) # Output : 25 

# x = 'This is the new value' # Output : This is te new value

# print(x)

# # Multiple Assignment with Same Value

# a = b = c = 100

# print(a,b,c)

# print(a,' ' ,b,' ',      c)

# print(a+b+c)

# print('a = ',a)

# # Multiple Assignement with different value 

# x,y,z = 1,1.25,'Python'

# print(x,y,z)

# # x=1,y=2.3,z=6.4 This is an error

# print(x,y,z)


# # Casting Variables and Using Type funtion to check their data type

# s = "10" # string

# print("s type is : ",type(s))
 
# n = int(s) # Casting string to Integer

# print("n type is : ",type(n))

# cnt = 5 # Integer

# print("cnt type is : ",type(cnt))

# f = float(cnt) # Casting integer to float

# print("f type is : ",type(f))

# age = 25

# print("age type is : ",type(age))

# s2 = str(age) # Casting integer to string

# print("s2 type is : ",type(s2))

# # Scope of Varibles :  Local && Global

# def f():
#     # local Variable 
#     p = 'I am a Local Variable'
#     print(p)

# #Driver Code
# f()
# # print(p)  This will give error 

# q = "I am Global Variable"

# def a():
#     # Checking global variable her
#     q = 'Changing global variable' # it takes it as local variable 
#    # q += 'Changing global val in Local function' This throws error
#     print("Inside local function \t",q)

# a()
# q+= ' altering variable globally'

# print(q)



a = 1

# Uses global 'a' as there is no local 'a'
def f():
    print("Inside f() : ",a)

# Variable 'a' is redifined as local variable
def g():
    a = 2
    print("Inside g() : ",a)

# Global Variable is accessed using global keyword and value is changed locally
def h():
    global a
    a = 3
    print("Inside h() : ",a)


#Checking the value change Golbally and in functions
print("global a : ",a)
f()
print("global a : ",a)
g()
print("global a : ",a)
h()
print("global a : ",a)

# Using del keyword to delete variable
del a


