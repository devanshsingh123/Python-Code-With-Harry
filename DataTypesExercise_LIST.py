# 📝 List Exercises
# 1️⃣ Find the Maximum & Minimum in a List

# Write a program that takes a list of numbers and prints the maximum and minimum values.
# Example Input: [10, 5, 20, 8, 25]
# Expected Output: Max: 25, Min: 5

# l1 = [2,5,27,45,2,47]
# max_value = float('-inf')
# min_value = float('inf') 

# # Feedback
# # Use direct looping ex- for num in l1: instead of using range
# # Use max and min function . predefined Python functions.
# for i in range(len(l1)):
#     if(max_value <= l1[i]):
#         max_value = l1[i]
#     if(min_value >= l1[i]):
#         min_value = l1[i]

# print("MAX_VALUE: ",max_value,", MIN_VALUE: ",min_value)



# 2️⃣ Remove Duplicates from a List

# Write a program that removes duplicate elements from a given list.
# Example Input: [1, 2, 2, 3, 4, 4, 5]
# Expected Output: [1, 2, 3, 4, 5]


# # Brute approach

# l1 = [1, 2, 2, 3, 4, 4, 5]

# output = []

# for val1 in l1:
#     isDuplicate = False
#     for val2 in output:
#         if(val2 != val1):
#             continue
#         else:
#             isDuplicate = True
    
#     if(not isDuplicate):
#         output.append(val1)


# print(output)  


# #Optimised Approach


# l1 = [1, 2, 2, 3, 4, 4, 5] 

# my_set = set()

# for val in l1:
#     my_set.add(val)

# print(my_set)


# Feedback 

# Use not in instead of flag

# l1 = [1, 2, 2, 3, 4, 4, 5]
# output = []

# for val in l1:
#     if val not in output:
#         output.append(val)

# print(output)  # Output: [1, 2, 3, 4, 5]


# Feedback on Optimised Approach

# l1 = [1, 2, 2, 3, 4, 4, 5]
# output = list(dict.fromkeys(l1))  # Preserves order

# print(output)  # Output: [1, 2, 3, 4, 5]

# The method dict.fromkeys(iterable, value) creates a dictionary where keys come from an iterable and values are set to the same default value (None if not provided).

# 🔹 Example 1: Basic Usage

# keys = ['a', 'b', 'c']
# new_dict = dict.fromkeys(keys)
# print(new_dict)  

# # Output: {'a': None, 'b': None, 'c': None}


# 🔹 Example 2: Setting Default Value


# keys = ['a', 'b', 'c']
# new_dict = dict.fromkeys(keys, 0)
# print(new_dict)  

# # Output: {'a': 0, 'b': 0, 'c': 0}


# 🔹 Example 3: Removing Duplicates from a List While Keeping Order
# Since keys in a dictionary must be unique, using dict.fromkeys() on a list automatically removes duplicates while maintaining order.

# l1 = [1, 2, 2, 3, 4, 4, 5]

# unique_list = list(dict.fromkeys(l1))
# print(unique_list)  

# # Output: [1, 2, 3, 4, 5]



# 🚀 Best Approach to Remove Duplicates Without Using dict.fromkeys()
# Using set() alone is fastest (O(n)) but does NOT maintain order.
# If you want both efficiency and order, use set() + list comprehension.

# ✅ Optimized Solution (Efficient and Order-Preserving)

# l1 = [1, 2, 2, 3, 4, 4, 5]
# seen = set()  # Stores unique elements

# unique_list = [x for x in l1 if not (x in seen or seen.add(x))]

# print(unique_list)  # Output: [1, 2, 3, 4, 5]


# 🛠 How It Works?

# seen = set() → Keeps track of unique elements.

# List comprehension:
# Condition: x not in seen or seen.add(x)
# If x is not in seen, add it to seen and keep it in the list.
# If x is already in seen, skip it.
# ⏳ Time Complexity:
# O(n) (Only one pass through the list, unlike brute-force O(n²)).
