# Goal: Create a parent class Employee.

# Attributes: name, salary.

# Inheritance: Create a child class Manager that inherits from Employee.

# New Attribute: Add a department attribute to the Manager (you may need to use super().__init__() or just set it manually for now).

# Test: Create a Manager and print their name, salary, and department.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, department, name, salary):
        self.department = department
        super().__init__(name, salary)


manager = Manager("IT", "F Rubena", 400000)
print(f"{manager.name} earns {manager.salary} and is from the {manager.department} department")

# F Rubena earns 400000 and is from the IT department
