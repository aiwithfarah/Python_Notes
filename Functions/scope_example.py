# It basically means : Where does a variable live?
# Local Scope: Variables created inside a function belong only to that function. The outside world cannot see them.
# Global Scope: Variables created outside any function are visible to everyone.

# Coding Challenge
# Challenge 1: The Invisible Variable
# Define a function called secret_function.
# Inside it, create a variable password = "1234" and print it.
# Call the function.
# Comment out a line below it where you try to print(password) from outside, just to acknowledge you know it would fail.

def secret_function():
    password = "1234"
    print(password)


secret_function()
# print(password)


# Challenge 2: Global vs Local
# Create a global variable city = "Delhi".
# Define a function change_city() that creates a local variable city = "Mumbai" and prints it.
# Call the function.
# Print city again outside the function to prove the global one didn't change.

city = "Delhi"


def change_city():
    city = "Mumbai"
    print(city)


change_city()  # Mumbai
print(city)  # Delhi
