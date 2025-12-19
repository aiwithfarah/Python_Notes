# Create a Parent class called Employee.
# Inside __init__, accept name and salary
# Make the salary a private variable (using __).
# Create a method called get_salary that returns the private salary.
# Create a Child class called Manager that inherits from Employee.
# Override the get_salary method.
# Inside this new method, return the private salary plus 5000 (Managers get a bonus!).
# Hint: Since the salary is private, even the Child class might struggle to touch self.__salary directly.
#  In Python, a Child usually calls self.get_salary() from the parent to get the base number, then adds to it.
# (If that hint is too confusing, just create a new method in Manager called get_total_pay that prints "I get a bonus")

# NOTE : Private variables are so secret that even the Child class (Manager) is not allowed to touch them directly.
#  Only the Employee class (where it was born) can touch it.
# Since Manager cannot touch __salary, it has to ask the Parent (Employee) to get the number.
#  We do this using a special command called super().
# super() = "Go to my Parent class."

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary


class Manager(Employee):

    # 1. Use super() to call the Parent's get_salary method
    def get_salary(self):
        base_salary = super().get_salary()
        return base_salary + 5000

    def get_total_pay(self):
        print("I get a bonus")


employee = Employee("Bob", 500000)
print(employee.get_salary())

manager = Manager("Alice", 50000)
print(manager.get_salary())


# Classes & Objects (Blueprints & Robots)

# Attributes (__init__ & self)

# Methods (Actions)

# Inheritance (Parents & Children)

# Polymorphism (Overriding methods)

# Encapsulation (Private __ variables)

# Super() (Calling the parent)
