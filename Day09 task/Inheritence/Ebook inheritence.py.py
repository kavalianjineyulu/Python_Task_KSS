
# Base class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


# Derived class
class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def display_ebook(self):
        self.display_book()
        print("File Size:", self.file_size, "MB")


# Create EBook object
ebook1 = EBook("Python Programming", "John", 500, 25)

# Display details
ebook1.display_ebook()
