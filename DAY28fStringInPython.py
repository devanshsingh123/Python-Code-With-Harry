# Old way  of using inputs in a string not very convinent way hence the use of f string

letter = "Hey My name is {1} and I am from {0}"

country = "India"
name = "Devansh"

print(letter.format(country,name))

# use of f string

print(f"Hey My name is {name} and I am from {country}")

# Example 2

txt = "For only {price:.2f} dollars!"

print(txt.format(price = 49.0999999))

price = 54.0999999

txt2 = f"For only {price:.2f} dollars!"

print(txt2)