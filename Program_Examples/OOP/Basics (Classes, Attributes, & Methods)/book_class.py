# 1. The Book Class

# Goal: Create a class called Book.

# Attributes: title, author, pages.

# Methods: Create a method called info() that prints: "[Title] by [Author], [Pages] pages."

# Test: Create two different books and call info() on both.

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")


book1 = Book("Farah's Life", "F Rubena", 16)
book2 = Book("The Master of the Game", "Sidney Sheldon", 116)
book1.info()
book2.info()

# Farah's Life by F Rubena, 16 pages
# The Master of the Game by Sidney Sheldon, 116 pages
