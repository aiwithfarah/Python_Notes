employees = ["Sam", "Bam", "Tam"]

file_path = "File Handling/output.txt"

with open(file_path, "w") as file:
    for emp in employees:
        file.write(emp + " ")
