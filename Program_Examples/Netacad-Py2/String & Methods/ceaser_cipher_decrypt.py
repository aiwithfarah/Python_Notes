# Ceaser cypher  decrypt a message

cipher = input("Enter cypher t be decrypted: ")
text = ""

for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
