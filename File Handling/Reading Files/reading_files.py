# python reading files (txt, csv, json)

file_path = "File Handling/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You do not have permission to read that file")
