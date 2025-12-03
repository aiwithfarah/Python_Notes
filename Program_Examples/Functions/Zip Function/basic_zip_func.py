# zip stops automatically when the shortest list runs out. It doesn't throw an error; it just ignores the extras

names = ["Alice", "Bob", "Charlie"]
ages = [22, 23, 25]
combined = list(zip(names, ages))
print(combined)  # [('Alice', 22), ('Bob', 23), ('Charlie', 25)]
