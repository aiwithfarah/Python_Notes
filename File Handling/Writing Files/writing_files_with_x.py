text = "Lorem Ipsum"

file_path = "File Handling/output.txt"

try:
    with open(file_path, "x") as file:
        file.write(text)
        print(f"Text File {file_path} was created")

except FileExistsError:
    print("File Already Exists!")
