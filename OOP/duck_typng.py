# Another way to achieve polymorphism
# # Object must have minimum necessary atributes/ methods
# If it looks like a duck, quakcs like a duck then it must be a uck

class Animal:

    alive = True


class Dog(Animal):

    def speak(self):
        print("Woof")


class Cat(Animal):

    def speak(self):
        print("meow")

# add a class that has nothing to do with animals


class Car:

    alive = False

    def speak(self):  # since it has the minimum necessary method (speak()) it will be considered an animal
        print("Honk")


# create a list of animals
animals = [Dog(), Cat(), Car()]  # create a fod and cat object

for animal in animals:
    animal.speak()
    print(animal.alive)
