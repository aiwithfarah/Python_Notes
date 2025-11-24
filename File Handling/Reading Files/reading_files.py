# python reading files (txt, csv, json)

file_path = "File Handling/Writing Files/output.txt"

try:
    with open(file_path, "r") as file:
        single_line = file.readline()  # Sam Bam Tam
        first_ten = file.read(10)  # Sam Bam Ta
        content = file.read()
        print(single_line)
        print(first_ten)
        print(type(single_line))  # <class 'str'>
        print(content)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You do not have permission to read that file")
