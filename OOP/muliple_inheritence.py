# parent class
class Prey:
    def flee(self):
        print("This animal is fleeing!")


# parent class

class Predator:
    def hunt(self):
        print("This animal is hunting!")


# child class
class Rabbit(Prey):
    pass


# child class
class Hawk(Predator):
    pass

# child class


class Fish(Prey, Predator):
    pass


# creating objects
rabit = Rabbit()
hawk = Hawk()
fish = Fish()

rabit.flee()  # This animal is fleeing!
hawk.hunt()  # This animal is hunting!
fish.hunt()  # This animal is hunting!
fish.flee()  # This animal is fleeing!
