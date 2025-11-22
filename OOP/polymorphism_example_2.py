class Animal:

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method!")


class Dog(Animal):

    def speak(slef):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow"


class Fish(Animal):

    def speak(self):
        return "Bubbles"


# create a list of diff animals
animals = [Dog(), Cat(), Fish()]

for animal in animals:
    print(animal.speak())
