# python reading files (txt, csv, json)

import csv

file_path = "File Handling/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You do not have permission to read that file")
