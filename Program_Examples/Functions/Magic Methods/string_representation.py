class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    # Magic method for printing
    def __str__(self):
        return f"A {self.color} {self.model}"


myCar = Car("Hyundai", "Zinc")
print(myCar)  # <__main__.Car object at 0x000001C327546A50>
# After adding __str__ hen we print the myCar object we get
# A Zinc Hyundai
