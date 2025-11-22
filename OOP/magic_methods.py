class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, keyword):
        return keyword in self.title

    def __getitem__(self, key):
        if key == "title":
            return self.title


book1 = Book("The Hidden Talent", "F ubena", 16)
book2 = Book("Harry Potter", "JK Rowling", 310)

print(book1)  # returns memory address <__main__.Book object at 0x000001CD8BE76A50>

# after adding __str__ we are able to return the string representaion
print(book1)  # The Hidden Talent by F ubena
print(book1 == book2)  # False
print(book1 < book2)  # True
print(book1 > book2)  # False
print(book1 + book2)  # 326
print("Hidden" in book1)  # True
print(book2['title'])  # Harry Potter
