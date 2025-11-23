import os

file_path = "File Handling/test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists.")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
    else:
        print("That is not a file")
else:
    print(f"The location {file_path} does not exist.")

# The location File Handling/test.txt exists.
# That is a file
