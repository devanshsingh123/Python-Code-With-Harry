class Smartphone:
    "A simple Smartphone model."

    category = "Electronics"

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def update_price(self, new_price):
        self.price = new_price



# ✅ Your Tasks:
# Use dir() on an instance of Smartphone and print out:

# All attributes and methods available (filter out the ones that don't start with double underscores __).

# Use __dict__:

# Print the instance variables after creating an object.

# Update the price using __dict__ without using any method.

# Use help():

# Print the documentation of the Smartphone class.

# 🎯 Bonus (Challenge):
# Dynamically add a new attribute color to the smartphone using __dict__ and print it.

# After adding, again print the updated __dict__.

# 📋 Example Expected Outputs
# dir() output ➔ ['brand', 'call', 'model', 'price', 'update_price']

# dict output ➔ {'brand': 'Apple', 'model': 'iPhone 14', 'price': 99999}

# help() output ➔ Shows the docstring "A simple Smartphone model."

s  = Smartphone("Apple", "iPhone 14", 99999)

print("dir() all output ->",dir(s))
print("dir() output that do not  starts with __ ➔", [attr for attr in dir(s) if not attr.startswith("__")])

print(s.__dict__)

s.__dict__["price"] = 109999

print(s.__dict__)

# print("help() output ➔", help(Smartphone))

print("help() output ➔", Smartphone.__doc__)

s.__dict__["color"] = "Black"

print(s.__dict__)

