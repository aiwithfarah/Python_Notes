import csv

employees = [["Name", "Age", "Place"], ["Farah", 34, "NYE"],
             ["Rusu", 6, "UAE"], ["Rube", 60, "NYE"]]

file_path = "File Handling/output.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"CSV File {file_path} was created")
