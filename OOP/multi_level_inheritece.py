class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")


class Prey(Animal):  # inherits from Animal Class

    def flee(self):
        print(f"{self.name} Fleeing!")


class Predator(Animal):  # inherits from Animal Class

    def hunt(self):
        print(f"{self.name} is hunting!")


class Rabit(Prey):  # inherits from Prey Class
    pass


class Fish(Prey, Predator):  # inherits from Prey & Predator Class
    pass


rabit = Rabit("Rabbie")
fish = Fish("Fishi")

rabit.eat()  # Rabbie is eating!
fish.eat()  # Fishie is eating!

fish.flee()  # Fishie is Fleeing!
fish.hunt()  # Fishie is hunting!
