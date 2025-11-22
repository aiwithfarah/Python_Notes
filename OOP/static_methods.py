# STATIC METHODS-Method that belongs to a class rather than any object from that class

# INSTANCE METHODS-Methods that belong to individual objects created from that class . Best for operations on instances of that class
# Static Methods: Bet for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # instance methof
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "CEO", "CTO", "CFO"]
        return position in valid_positions


print(Employee.is_valid_position("CEO"))
