f = open("manual_text_file.txt", "w")
f.write("This is a Test File")
f.close()

# OR
with open("output.txt", "w") as f:
    f.write("ola")

with open("output.txt", "r") as f:
    contents = f.read()
print(contents)
