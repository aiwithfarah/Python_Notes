# a - any new data will be apended to that file

text = "And I like Dark Chocolate"

file_path = "File Handling/output.txt"

try:
    with open(file_path, 'a') as file:
        file.write("\n" + text)
        print(f"{text} was appended to that file!")
except Exception:
    print("Something went wrong!")
