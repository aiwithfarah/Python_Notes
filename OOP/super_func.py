class Shape:

    def __init__(self, color, filled_in):
        self.color = color
        self.filled_in = filled_in


class Circle(Shape):
    def __init__(self, color, filled_in, radius):
        super().__init__(color, filled_in)
        self.radius = radius


class Square(Shape):
    def __init__(self, color, filled_in, width):
        super().__init__(color, filled_in)
        self.width = width


class Triangle(Shape):
    def __init__(self, color, filled_in, height, width):
        super().__init__(color, filled_in)
        self.height = height
        self.width = width


circle = Circle(color="red", filled_in=True, radius=5)
square = Square(color="yellow", filled_in=False, width=4)
triangle = Triangle(color="blue", filled_in=True, height=4, width=6)
print(circle.color)
print(circle.radius)
