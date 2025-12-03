# The "Log Reader" Challenge: I want you to write a generator function that simulates reading a large file.

# It should take a list of lines: ["Error: 404", "Info: Login", "Error: 500"].

# It should loop through them.

# It should yield a line only if it starts with "Error". (Combining filter logic inside a generator!)

def log_reader(error_list):

    for err in error_list:
        if err.startswith("Error"):
            yield err


logs = ["Error: 404", "Info: Login", "Error: 500"]
my_gen = log_reader(logs)
print(next(my_gen))
print(next(my_gen))

# Error: 404
# Error: 500
