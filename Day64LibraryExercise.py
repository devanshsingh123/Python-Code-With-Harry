# Write a Library class with no_of_books and books as two instance variables.
#  Write a program to create a library from this Library class and show how you can print all books, 
# add a book and get the number of books using different methods. Show that your program 
# doesnt persist the books after the program is stopped!



class Library:
    def __init__(self,books: list[str],no_of_books: int):
        self.books = books
        self.no_of_books = no_of_books

    def show_all_books(self):
        for book in self.books:
            print(book)
    
    def add_book(self,new_book):
        self.books.append(new_book)

    def total_books(self):
        print(f"Total books: {self.no_of_books}")

    def is_book_number(self):
        return len(self.books) == self.no_of_books

l1 = Library(["Kafka on the shore","Norweigian Wood","Thousand Splendid Suns"],3)

l1.show_all_books()

print(f"Is number books record correct : {l1.is_book_number()}")

l1.add_book("Kite Runner")

print(f"Is number books record correct : {l1.is_book_number()}")

l1.show_all_books()