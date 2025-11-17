# validate user input
# 1. name cannot be more than 12 char long
# 2. must not contain spaces
# 3. must not contain digits

name = input("Enter your name: ")

if len(name) <= 12 and not name.find(" ") == -1 and not name.isalpha():
    print(f"Welcome {name}")
else:
    print("You have not followed the rules for names")
