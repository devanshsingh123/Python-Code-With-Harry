# 🧪 Exercise: Create a Book Class with Multiple Constructors
# ✅ Requirements:
# Create a Book class with these attributes:
# title (string)
# author (string)
# price (float)
# year (int)
# The main constructor (__init__) should take all 4 parameters.
# Create two class methods:
# from_string(data_str: str) → Input format: "The Hobbit;J.R.R. Tolkien;350.50;1937"
# from_dict(data: dict) → Input format: {"title": "1984", "author": "George Orwell", "price": 250.0, "year": 1949}
# Implement a __str__() method to make the object print nicely:
# Format: "Book: <title> by <author> - ₹<price> (<year>)"

# 🎯 Bonus (Optional):
# Validate that the price is positive and the year is not in the future (2025+).
# If not, raise a ValueError.
import datetime


class Book:
    def __init__(self, title: str, author: str, price: float, year: int):
        self.title = title
        self.author = author
        if(price > 0):   
            self.price = price
        else:
            raise ValueError("Price must be positive.")
        if(year > datetime.datetime.now().year):
            raise ValueError("Year cannot be in the future.")
        else:
           self.year = year

    @classmethod
    def from_string(cls, data_str: str):
        title, author, price, year = data_str.split(";")
        return cls(title, author, float(price), int(year))

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["title"], data["author"], data["price"], data["year"])

    def __str__(self):
        return f"Book: {self.title} by {self.author} - ₹{self.price} ({self.year})"
    



b1 = Book.from_string("The Hobbit;J.R.R. Tolkien;350.50;1937")
b2 = Book.from_dict({
    "title": "1984",
    "author": "George Orwell",
    "price": 250.0,
    "year": 1949
})

print(b1)  # Book: The Hobbit by J.R.R. Tolkien - ₹350.5 (1937)
print(b2)  # Book: 1984 by George Orwell - ₹250.0 (1949)
