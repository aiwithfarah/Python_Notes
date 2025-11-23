# Goal: Create a parent class Vehicle with a method fare() that returns the cost of a ride (e.g., generic $5).

# Child Class: Create a Bus class that inherits from Vehicle.

# Logic: In Bus, override fare() so that it returns the parent's fare + an extra maintenance fee (e.g., total $5 + 50 cents).

class Vehicle:

    def __init__(self, cost_of_ride):
        self.cost_of_ride = cost_of_ride

    def fare(self):
        return self.cost_of_ride


class Bus(Vehicle):

    def __init__(self, cost_of_ride, maintenance):
        super().__init__(cost_of_ride)
        self.maintenance = maintenance

    def fare(self):
        return self.cost_of_ride + self.maintenance


bus = Bus(5, 50)
print(bus.fare())
