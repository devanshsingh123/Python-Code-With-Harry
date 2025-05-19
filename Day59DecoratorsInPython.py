def WrappedUse(func):
    def newfuntion():
        print("Unique UseCase to implement. So , code rgards to that")
        #calling this function as the common implementation is needed
        func()
        print("Some more impotant code after the common uscase code")

    return newfuntion



@WrappedUse
def work():
    print("Here the code of some important commaon work")


# work()

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        print(f"[LOG] Arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished function: {func.__name__}")
        return result
    return wrapper


@log_function
def greet(name):
    print(f"Hello, {name}!")


# greet("Devansh")    

import time
from functools import wraps

def detailed_logger(func):
    @wraps(func)  # Preserves original function name and docstring
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("="*50)
        print(f"📌 Function      : {func.__name__}")
        print(f"📥 Arguments     : {args} {kwargs}")
        print(f"⏱️ Started At     : {time.strftime('%X')}")
         
        result = func(*args, **kwargs)
        
        end_time = time.time()
        duration = end_time - start_time

        print(f"✅ Return Value  : {result}")
        print(f"⏳ Ended At       : {time.strftime('%X')}")
        print(f"🕒 Duration       : {duration:.6f} seconds")
        print("="*50)
        return result
    return wrapper

@detailed_logger
def compute_sum(n):
    time.sleep(1)  # Simulating a delay
    return sum(range(n))

compute_sum(1000000)