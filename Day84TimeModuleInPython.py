import time
import win32com.client as wincl


# t = time.time()
# l_t = time.localtime()
# gm_t = time.gmtime()

# print("Time in sceonds passed since the epoch: " ,t)
# print("Converts epoch time to a time struct (local): ", l_t)
# print("	Converts epoch time to UTC time struct: ",gm_t)5
# t_str = time.strftime("%Y-%m-%d %H:%M:%S",gm_t)
# print("Using strftime to covert time into desired format in string : ",t_str)

# time_string = "202557"

# str_c_time = time.strptime(time_string,"%Y%m%d")

# print(" string Converted into time result : ", str_c_time)


# # Using perf counter

# start = time.perf_counter()

# time.sleep(1.5) # This is used to pause the code

# end = time.perf_counter()

# print(f"{end-start:2f} seconds passed!")

# Time exercise:
# 🧠 Challenge: Countdown Timer with Elapsed Time Logger
# Task:
# Create a function that:

# Accepts a number of seconds as input.

# Displays a countdown in real time (e.g., Countdown: 5, then 4, etc.).

# When it finishes, prints:

# "Time's up!"

# The total time taken to run the countdown using time.perf_counter().
#MyCode
speak = wincl.Dispatch("SAPI.SpVoice")

count = int(input("Please provide the interger number for the  count : "))    
start = time.perf_counter()
end = ''
while(count > 0):
    if count == 1:
         time.sleep(1)
         print(count)
         speak.Speak(f"{count}")
         end = time.perf_counter() 
         speak.Speak("Times Up !")   
         print("Times Up !")
         break
    time.sleep(1)
    print(count)
    speak.Speak(f"{count}",3)
    count-=1
print(f"Total time taken: {end-start:2f} seconds")


#ChatGPT

speak = wincl.Dispatch("SAPI.SpVoice")
count = int(input("Please provide the integer number for the count: "))
start = time.perf_counter()

while count > 0:
    print(f"Countdown: {count}")
    if count == 1:
        speak.Speak(f"{count}")  # Blocking speak for the last second
    else:
        speak.Speak(f"{count}", 3)  # Async for others
    time.sleep(1)
    count -= 1

speak.Speak("Time's up!")  # Blocking to ensure it's heard
end = time.perf_counter()

print("Time's up!")
print(f"Total time taken: {end - start:.2f} seconds")
