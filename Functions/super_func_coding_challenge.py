# Challenge 1: The Parent Class
# Define a class Employee.
# It should have an __init__ that takes name and salary and saves them to self.
# Add a method show_details() that prints "Name: [name], Salary: [salary]".

# You only need super() if you decide to override the __init__ method because you want to
# add something new (like a department variable).

# The reason we did not need super() function in the child is because we added amount to a Method, not to the Object's Setup.
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Challenge 2: The Child Class
# Define a class Manager that inherits from Employee.
# Inside Manager, create a new method called give_bonus(amount).
# This method should print "Manager [name] gets a bonus of [amount]".


class Manager(Employee):

    def give_bonus(self, amount):
        print(f"Manager {self.name} gets a bonus of {amount}")


# Challenge 3: Putting it Together
# Create an object m1 from the Manager class (Name: "Farah", Salary: 100000).
# Call m1.show_details() (Inherited from Parent).
# Call m1.give_bonus(5000) (Specific to Child).
m1 = Manager("Farah", 1000000000)
m1.show_details()
m1.give_bonus(5000000)
