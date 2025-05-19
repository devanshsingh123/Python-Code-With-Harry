# 🔧 Syntax:

# variable := expression
# This assigns the result of expression to variable, and also returns the value.

# ✅ Common Use Cases:
# 1. While loop without repeating expression

# # Without walrus
# line = input("Enter something: ")
# while line != "quit":
#     print(f"You typed: {line}")
#     line = input("Enter something: ")

# # With walrus
# while (line := input("Enter something: ")) != "quit":
#     print(f"You typed: {line}")
# 2. Filtering with assignment

# # Without walrus
# results = []
# for value in data:
#     length = len(value)
#     if length > 3:
#         results.append((value, length))

# # With walrus
# results = [(value, length) for value in data if (length := len(value)) > 3]
# ⚠️ When not to use:
# Use the Walrus operator only when it increases clarity. Overusing it can lead to code that is hard to read.

