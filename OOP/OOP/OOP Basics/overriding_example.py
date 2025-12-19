# Sometimes, the Child doesn't want to do exactly what the Parent does.
# Inheritance = "I do what my parent does."
# Overriding = "I have the same skill as my parent, but I do it differently."
# This is technically called Polymorphism, but you can just think of it as "Updating the Method."
# If the Child has its own version of a method, Python uses that. If it doesn't, Python looks up at the Parent.

# <---------TASK----------->
# Create a Parent class Bird.
# Give it a method fly that prints "I am flying high!".
# Create a Child class Penguin that inherits from Bird.
# Override the fly method inside Penguin.
# It should print "I cannot fly, but I can swim."
# Create a Penguin object and call its fly method to prove it uses the new version.

class Bird:

    def fly(self):
        print("I am flying high!")


class Penguin(Bird):

    def fly(self):
        print("I cannot fly,but I can swim")


penguin = Penguin()
penguin.fly()  # I cannot fly,but I can swim
