# # ✅ Generators in Python
# # Generators are a simple and memory-efficient way to create iterators.
# #  Instead of holding all values in memory at once (like a list), 
# # a generator yields values one by one, only when needed.

#  Why use Generators?
# Save memory when dealing with large data (e.g. reading large files, streams).

# Provide lazy evaluation – data is generated on the fly.

# Make iterators easy to write using yield.

# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1

# gen = count_up_to(5)
# for num in gen:
#     print(num)
