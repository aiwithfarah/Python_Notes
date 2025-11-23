# Goal: Create a class User.

# Attributes: username (public) and __password (private).

# Methods:

# check_password(input_pass): Returns True if the input matches the private password, False otherwise.

# change_password(new_pass): Updates the private password.

# Test: Try to access user.__password directly (it should fail), then use the methods to check it.

class User:

    def __init__(self, username, password):
        self.username = username
        # use 2 underscores to make the variable inaccessible from outside
        self.__password = password

    def check_password(self, input_item):
        if input_item == self.__password:
            return True
        return False

    def change_password(self, new_pass):
        self.__password = new_pass
        print(new_pass)


user = User("Farah", "rube")
# print(user._password)
print(user.check_password("abba"))  # False
user.change_password("RUBE")  # RUBE
