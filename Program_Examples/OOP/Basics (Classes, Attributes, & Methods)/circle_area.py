# Goal: Create a class Circle.
# Attributes: radius.
# Methods: get_area(): Returns pi r2 (Use 3.14 for pi).get_circumference(): Returns 2pir.Test:
# Calculate details for a circle with radius 7.

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius**2

    def get_circumference(self):
        return 2 * 3.14 * self.radius


circle = Circle(7)
print(circle.get_area())
print(circle.get_circumference())
