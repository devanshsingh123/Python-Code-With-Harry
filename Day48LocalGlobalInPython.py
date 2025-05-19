x = 4
print(x)

def hello():
    global x 
    x = 6 
    print(f"The local variable x value is {x}")
    print("Hello Devansh")

print(f"The globle variable x is: {x}")
hello()
# x = 5
print(f"The global x is: {x}")
