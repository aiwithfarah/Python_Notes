# Sometimes the Child wants to do what the Parent does, plus a little extra.
# super() gives you access to the Parent class.
# We often use super().__init__(...) to make sure the Parent sets up its part of the data before we add ours.

class Employee:

    def __init__(self, name):
        self.name = name
        print("W")


class Manager(Employee):
    def __init__(self, name, department):
        # Call parent's __init__ to handke the name
        super().__init__(name)

        # Now handle manager specific properties
        self.department = department
        print('Manager Ready!')


m = Manager("Farah", "Tech")
print(m.name)
print(m.department)

# Manager Ready!
# Farah
# Tech
