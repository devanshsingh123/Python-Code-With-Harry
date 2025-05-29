# Multithreading in Python allows you to run multiple threads (smaller units of a process) at the same time, 
# which can be useful for I/O-bound tasks like file reading, network operations, or user input handling.

# 🧠 What is a Thread?
# A thread is a lightweight, separate flow of execution. 
# All threads of a process share the same memory space.

# 🔧 When to Use Multithreading?
# Use multithreading when:

# Your program waits for things (disk I/O, API calls, file reads/writes, etc.)
# You want to keep the application responsive (e.g., GUI apps or real-time I/O)
# ❗ Not ideal for CPU-heavy tasks due to the Global Interpreter Lock (GIL) in CPython.
# Multithreading in Python allows you to run multiple threads (smaller units of a process) at the same time,
# which can be useful for I/O-bound tasks like file reading, network operations, or user input handling.

# 🧠 What is a Thread?
# A thread is a lightweight, separate flow of execution. All threads of a process share the same memory space.

# 🔧 When to Use Multithreading?
# Use multithreading when:

# Your program waits for things (disk I/O, API calls, file reads/writes, etc.)
# You want to keep the application responsive (e.g., GUI apps or real-time I/O)

# ❗ Not ideal for CPU-heavy tasks due to the Global Interpreter Lock (GIL) in CPython.

# 📋 Useful Threading Concepts
# Feature	Description
# start()	Starts the thread
# join()	Waits for thread to finish
# is_alive()	Checks if the thread is still running
# current_thread()	Returns the current thread object


# 🚫 Limitation: GIL
# Python’s Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode at a time.

# This makes threading less useful for CPU-bound tasks (use multiprocessing instead).



import threading
import time

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)

# # Create a thread
# t = threading.Thread(target=print_numbers)

# # Start the thread
# t.start()

# # Main thread continues
# print("Main thread is running...")

# # Wait for thread to finish
# t.join()
# print("Thread finished.")


def task(name):
    for i in range(3):
        print(f"{name} is working...")
        time.sleep(1)

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()
print("Both threads completed.")



