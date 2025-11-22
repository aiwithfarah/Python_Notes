class Animal:

    def __init__(self, name):
        self.name = name

    def is_sleeping(self):
        print(f"{self.name} is sleeping")

    def is_eating(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    pass


class Cat(Animal):

    def is_eating(self):
        print(f"{self.name} is not eating")


kitty = Cat("kittu")
doggie = Cat("doggu")
print(kitty.name)  # kittu
print(doggie.name)  # doggie

doggie.is_eating()
kitty.is_eating()  # kittu is not eating
