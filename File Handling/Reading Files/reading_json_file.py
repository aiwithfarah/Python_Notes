# python reading files (txt, csv, json)

import json

file_path = "File Handling/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You do not have permission to read that file")
