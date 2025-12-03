# Match case introduced in Python 3.10
# it compare a value against multiple patterns and executes the matching case block

command = "learn"

match command:
    case "run":
        print("Start running")
    case "dance":
        print("Start Dancing")
    case "learn":
        print("Start Learning")
    case "fight":
        print("Start fighting")

# Start Learning

# range() returns an iterable of numbers

# enumerate -> retrieves both index and the value of each list item
animals = ["mittu", "chittu", "pittu"]

for i, value in enumerate(animals):
    print(i, value)

# 0 mittu
# 1 chittu
# 2 pittu
