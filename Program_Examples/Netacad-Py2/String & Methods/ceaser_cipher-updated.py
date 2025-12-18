# The idea is rather simple – every letter of the message is replaced by its nearest consequent
#  (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.

text = input("Enter the text to be encrypted: ")
cipher = ""

while True:
    try:
        shift_value = int(
            input("Enter a shift value: between 1 and 25 (inclusive) "))
        if 1 < shift_value < 25:
            break
        else:
            print("Enter a number specifically between 1 and 25: ")

    except ValueError:
        print("You can only enter numbers between 1 and 25 ")

for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + shift_value
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
