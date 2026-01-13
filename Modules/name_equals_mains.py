# When you import a file, Python actually runs all the code inside it immediately.
# Python has a special if statement to say: "Only run this code if I execute this file directly.
# Do NOT run it if I am being imported.

def add(a, b):
    return a + b


if __name__ == "__main__":
    print(f'Testing Adition : ${add(1, 2)}')  # Testing Adition : $3
