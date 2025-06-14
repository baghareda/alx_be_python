class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_out(self):
        self._is_checked_out = True
        
    def return_book(self):
        self._is_checked_out = False
        
    def is_availble(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_availble():
                book.check_out()
                return
            
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_availble():
                book.return_book()
                return
            
    def list_available_books(self):
        for book in self.books:
            if book.is_availble():
                print (f"{book.title} by {book.author}")
            
    