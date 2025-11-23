import json

employee = {
    "name": "Farah",
    "age": 34,
    "job": "Entrepreneur"
}

file_path = "File Handling/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"Json File {file_path} was created!")
except FileExistsError:
    print("File Already Exists!")
