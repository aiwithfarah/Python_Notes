# # poly = many
# # morph = forms

# 2 Ways to achieve polymorphism: 1. Through inheritence 2. Duck Typing

class Shape:

    def area(self):
        pass


class Circle(Shape):
    pass


class Square(Shape):
    pass


class Triangle(Shape):
    pass


circle = Circle()  # here our circle object as 2 forms: its a Circle and its a Shape

# create a list of shapes
shapes = [Circle(), Square(), Triangle()]
