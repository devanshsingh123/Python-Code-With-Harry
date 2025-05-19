# def recursiveDivide(n):
#     if n < 10:
#         return
#     print(n)
#     recursiveDivide(n/2)



# recursiveDivide(2000)

# 5!  5*4*3*2*1  n*n-1 till n<1 return 


def factorial(n):
    if n==1 and n==0:
        return 1
    value = n * factorial(n-1)
    return value


#print(factorial(5))

def fibonacci(n):
    if n==1 :
        return 1
    elif n <= 0:
        return 0
    return(fibonacci(n-1) + fibonacci(n-2))  
    


print(fibonacci(5))
    