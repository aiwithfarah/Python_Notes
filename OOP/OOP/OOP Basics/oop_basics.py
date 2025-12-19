# Methods

# Write the Cat class with __init__ (accepting name and age).
# Add a new method called speak.
# Inside speak, make it print: "Meow! My name is [insert name here]".
# Create a cat object named simba with the name "Simba" and age 5.
# Call the speak method for simba.

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Meow. My name is {self.name}")


simba = Cat("Simba", 5)
simba.speak()
