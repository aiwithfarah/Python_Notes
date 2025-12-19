# Encapsulation is the practice of hiding variables so they cannot be changed directly from outside the object.
# We "protect" them.
# In Python, if you put two underscores __ in front of a variable name, Python hides it.

# <--------TASK--------------->
# Create a class Phone.
# Inside __init__, create a private variable called __number (use the double underscore) and set it to "123-4567".
# Try to print my_phone.__number directly. (I expect this to fail/crash—that is the point!)
# Comment out the crashing line, and instead write a method called get_number that returns the number.
# Call get_number and print the result.

class Phone:

    def __init__(self):
        # The __ make it a pivate variable
        self.__number = "123-4567"

    # Since numbe is hidden we need a method to show it to us
    def get_number(self):
        return self.__number


phone = Phone()
# If we try to touch the number directly, Python pretends it doesn't exist!Hence we must use the method
print(phone.get_number())

# Why do this?
# It forces programmers to use your methods (like deposit or withdraw) instead of messing with the data directly.
# It keeps the logic safe.
