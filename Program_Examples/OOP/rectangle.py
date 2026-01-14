# Create a class Rectangle.
# __init__: Takes length and width.
# Method area(): Returns length * width.
# Method perimeter(): Returns 2 * (length + width).

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(2, 2)
print(rect.area())
print(rect.perimeter())
