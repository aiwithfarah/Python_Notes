# Imagine you have a list of book titles that are written in all lowercase letters (whispering).
# #  You need to "fix" the catalog by making every title uppercase (shouting) for a display.
# Input: ["the hobbit", "1984", "the great gatsby"]

# Challenge: Convert every string in the list to uppercase.

# Goal: Practice string methods within a map function.

book_list = ["the hobbit", "1984", "the great gatsby"]

loud_books = list(map(lambda x: x.upper(), book_list))

print(loud_books)  # ['THE HOBBIT', '1984', 'THE GREAT GATSBY']
