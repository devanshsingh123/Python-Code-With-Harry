# ✅ Asyncio in Python – Overview
# asyncio is a standard Python library used for writing concurrent 
# code using the async/await syntax. It's ideal for I/O-bound tasks like:

# Network operations

# File I/O

# API calls

# Waiting without blocking other tasks


# 🔹 Why Use asyncio?
# Traditional Python executes code line by line (synchronously).
#  If one line takes time (e.g., a web request), everything else waits.

# With asyncio, you can run multiple I/O-bound tasks concurrently without creating threads.

# 🔹 Real World Use Case

# Web scrapers fetching from multiple URLs
# Chat apps waiting for messages
# Servers handling many clients
# Timers, countdowns, and delayed jobs

# 🔸 Common Terms

# Term	                   Meaning
# coroutine	        An async function
# await	                Waits for a coroutine to complete
# asyncio.run()	        Runs the event loop
# asyncio.gather()	Runs multiple coroutines concurrently
# asyncio.sleep()	Non-blocking delay

# import time
# import asyncio

# async def func1():
#         print("funcion 1 started")
#         await asyncio.sleep(8)
#         print("funcion 1 completed")

# async def func2():
#         print("function 2 started")
#         await asyncio.sleep(6)
#         print("function 2 completed")

# async def func3():
#         print("function 3 started")
#         await asyncio.sleep(3)
#         print("function 3 completed")



# async def main():
#         # await func1()
#         # await func2()
#         # await func3()
#         await asyncio.gather(func1(),func2(),func3())


# asyncio.run(main())



# 🔧 Exercise: Simulate an Asynchronous Download Manager
# 🧩 Goal:
# Simulate downloading 5 files asynchronously. Each file takes a random amount
#  of time to download (between 1 and 5 seconds). After all downloads complete, display the total time taken.

# 📝 Requirements:
# Use asyncio.sleep() to simulate file download time.

# Use asyncio.gather() to run all downloads concurrently.

# Print a message:

# When each file starts downloading

# When each file finishes downloading

# Show total elapsed time after all downloads are done.


# import time
# import asyncio
# import random

# async def download(file_name: str):
#     print(f"Download of {file_name} started...")
#     start = time.perf_counter()
#     delay = random.randint(1, 10)
#     await asyncio.sleep(delay)
#     end = time.perf_counter()
#     print(f"Download of {file_name} completed in {end - start:.2f} seconds.")

# async def main():
#     start = time.perf_counter()
    
#     tasks = [
#         download("file1.txt"),
#         download("file2.txt"),
#         download("file3.txt"),
#         download("file4.txt"),
#         download("file5.txt"),
#     ]
    
#     await asyncio.gather(*tasks)
    
#     end = time.perf_counter()
#     print(f"All downloads finished in {end - start:.2f} seconds.")

# asyncio.run(main())

# 🧠 What is aiohttp?
# aiohttp is an asynchronous HTTP client/server library for Python, built on top of asyncio.
# It allows you to send HTTP requests and build HTTP servers non-blockingly.
# Unlike requests (which is synchronous), aiohttp can perform multiple network operations concurrently,
#  making it much faster for I/O-bound tasks like:
# Downloading files
# Scraping data
# Sending API requests

import aiohttp
import asyncio
import time
from pathlib import Path

# List of sample image URLs (you can change/add more)
urls = [
    "https://via.placeholder.com/300.png",
    "https://via.placeholder.com/400.png",
    "https://via.placeholder.com/500.png",
    "https://via.placeholder.com/600.png",
    "https://via.placeholder.com/700.png",
]

# Save files in 'downloads' folder
download_folder = Path("downloads")
download_folder.mkdir(exist_ok=True)

async def download_file(session, url):
    filename = download_folder / url.split("/")[-1]
    print(f"Starting download: {filename.name}")
    start = time.perf_counter()
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.read()
            filename.write_bytes(content)
            end = time.perf_counter()
            print(f"Finished: {filename.name} in {end - start:.2f} sec")
        else:
            print(f"Failed to download {url}: Status {response.status}")

async def main():
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url) for url in urls]
        await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"\nAll downloads completed in {end - start:.2f} seconds.")

asyncio.run(main())
