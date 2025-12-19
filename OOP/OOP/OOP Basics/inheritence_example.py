# Create a Parent class called Vehicle.
# Give it a method called drive that prints "The vehicle is moving."
# Create a Child class called Car that inherits from Vehicle. (class Car(Vehicle):)
# Give the Car its own method called honk that prints "Beep beep!"
# Create an object called my_car from the Car class.
# Call both methods:
# Make my_car honk.
# Make my_car drive (showing it inherited the ability).

class Vehicle:

    def __init__(self):
        pass

    def drive(self):
        print("The Vehicle is moving.")


class Car(Vehicle):

    def honk(self):
        print("Beep, beep!")


my_car = Car()
my_car.drive()
