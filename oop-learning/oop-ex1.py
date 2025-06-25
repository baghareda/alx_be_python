class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return (f"the book you choosed title is: {self.title} ,by: {self.author} that has: {self.pages} pages.")
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.pages})'"
    
title = "sadimadi"
author = "dawimawi"
pages = 8000

