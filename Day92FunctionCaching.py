# 🚀 Function Caching in Python
# Function caching (also known as memoization) is a powerful technique to speed up programs
# by storing the results of expensive function calls and reusing the cached result when the 
# same inputs occur again.

# ✅ Why Use It?

# Avoid recomputing the same results.
# Improves performance, especially for recursive functions or heavy calculations.
# Makes functions more efficient with repeated inputs.


# Python provides built-in support for caching with functools.lru_cache.
# Without caching, calculating fib(40) recursively would take a long time.
# With caching, it stores results and avoids redundant calls.


from functools import lru_cache

@lru_cache(maxsize=None)  # You can also set a maxsize, e.g., 100
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
