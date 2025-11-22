# @property - used to define a method as a property(must be accessed like an attribute)
# gives us a getter method to read a setter to write an deleter method to delete

class Reactangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    @property
    def height(self):
        return f"{self._height:.2f}cm"


rect = Reactangle(3, 4)

print(rect.height)  # 4.00cm

print(rect.width)  # 3.00cm
