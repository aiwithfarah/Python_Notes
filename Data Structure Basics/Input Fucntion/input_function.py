# Used to accepts input from a user - returns a string

name = input("What is your name: ")
age = int(input("Enter your age: "))

print(type(name))  # <class 'str'>

print(f"Hello, {name}, you are {age + 1} years old!")
# Hello, farah, you are 34 years old!
