# executes a block of code until the condition remains true

x = 0

while x < 5:
    print(f"Current value : {x}")
    x += 1
else:
    print(f"{x} Is not Less than 5")

# Current value : 0
# Current value : 1
# Current value : 2
# Current value : 3
# Current value : 4
# 5 Is not Less than 5


name = input("Enter your name: ")

while name == "":
    print("You did not enter a name!")
    name = input("Enter your name: ")
print(f"Hello {name}")


food = input("Enter a food your like (q to quit): ").lower()

while food != 'q':  # while not food == 'q'
    print(f"You like {food}")
    food = input("Enter another food you like: ")
print("bye")


num = int(input("Enter a num between 1 & 10: "))

while num < 1 or num > 10:
    print("You've en    tered an invalid number")
    num = int(input("Enter another num between 1 & 10: "))
print("Exit")
