class Book:
    def __init__(self,title,author):
        self.author = author
        self.title = title
    def type(self):
        return 1
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def type(self):
        return 3
class PrintBook(Book):
    def  __init__(self, title, author,page_count):
        super().__init__(title, author)   
        self.page_count = page_count
    def type(self):
        return  2
class Library():
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        # if book.type == 1 :
        #     print(f"Book: {book.title} by {book.author}")
        # if book.type == 2 :
        #     print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}")
        # if book.type == 1 :
        #     print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
    def list_books(self):
        for book in self.books :
            if book.type == 1 :
                print(f"Book: {book.title} by {book.author}")
            if book.type == 2 :
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}")
            if book.type == 1 :
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")

