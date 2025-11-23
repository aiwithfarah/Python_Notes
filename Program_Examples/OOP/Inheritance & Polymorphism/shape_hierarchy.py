# Goal: Create a parent class Shape with a method describe() that prints "I am a shape".

# Inheritance: Create a child class Square that inherits from Shape.

# Polymorphism: Override the describe() method in Square to print "I am a square".

# Test: Create a Square object and call describe().

class Shape:

    def describe(self):
        print("I'm a shape")


class Square(Shape):

    # Polymorphism here is achieved by overriding a method that originally belongs to a parent class in the child class
    def describe(self):
        print("I am a square")


square = Square()
square.describe()  # I am a square
