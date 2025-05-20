# ✅ Regular Expressions in Python (with re module)
# Regular expressions (regex) are a way to define search patterns, 
# primarily used for pattern matching in strings — useful for validation, 
# extraction, and substitution.

# 🔹 2. Common Functions in re
# Function	Description
# re.match()	Match from the start of the string
# re.search()	Search anywhere in the string
# re.findall()	Returns all matches as a list
# re.finditer()	Returns match objects (iterable)
# re.sub()	Replaces matched patterns

# 🔹 3. Basic Pattern Symbols
# Pattern	Meaning
# .	Any character except newline
# ^	Start of string
# $	End of string
# *	0 or more
# +	1 or more
# ?	0 or 1
# \d	Digit (0–9)
# \D	Not a digit
# \w	Word character
# \s	Whitespace
# [abc]	a, b, or c
# [^abc]	Not a, b, or c
# {m,n}	Between m and n times


# 🔹 4. Example Usages
# ✅ Validate Email
import re
# email = "user@example.com"
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")


# ✅ Extract all numbers

# text = "There are 3 apples for $5.50"
# print(re.findall(r'\d+\.?\d*', text))  # ['3', '5.50']

# ✅ Replace words

# text = "Python is great"
# new_text = re.sub(r'Python', 'Java', text)
# print(new_text)  # Java is great

# 🔹 5. Match Object

# match = re.search(r'\d+', "There are 5 apples")
# if match:
#     print(match.group())     # 5
#     print(match.start())     # Index



# 🔸 1. Email Validator
# Write a regex to check if a string is a valid email address.

# Test Strings:

email = '2test@example.com'

# john.doe@my-site.co

# bad-email@.com

# ✅ Expected: Match only valid emails.

pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

if re.match(pattern,email):
    print("email Valid")
else:
    print("email InValid")
