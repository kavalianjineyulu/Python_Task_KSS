class Book:
    def __init__(self, tittle, author, price):
        self.tittle = tittle
        self.author = author
        self.price = price
    def display_book(self):
        print("Book title:",self.title)
        print("author:", self.auuthor)
        print("price:", self.price)
class Ebook(Book):
    def __init__(self, title, suthor, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size
    def display_ebook(self):
        self.display_book()
        print("file size:", self.file_size, "MB")
ebook1 = EBook("python programming","john",500,25)
ebook1.display_ebook()
