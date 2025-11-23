# 3. The Rectangle Area

# Goal: Create a class called Rectangle.

# Attributes: length, width.

# Methods: Create a method area() that calculates and returns the area (length * width).

# Test: Create a rectangle with length 10 and width 5. Print the area.


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(10, 5)
print(rect.area())
