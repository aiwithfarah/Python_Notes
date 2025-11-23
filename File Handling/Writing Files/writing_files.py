# python writing files(.json, .txt..csv)

text = "I like piza"
file_path = "File Handling/output.txt"

with open(file_path, "w") as file:
    file.write(text)
    print(f"Text File {file_path} was created")
