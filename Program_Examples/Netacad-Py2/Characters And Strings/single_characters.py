# # Computers store characters as numbers
# The ASCII Standard: To ensure different computers and operating systems can communicate,
# a universal standard called ASCII (American Standard Code for Information Interchange) was adopted.

# Key Details: ASCII defines 256 characters. The most common character, the space, is represented by the number 32.
# use ord() function to convert any sequence into ASCII number sequence

name = "farah"

for i in name:
    print(f"Char: {i} --> ASCII Number: {ord(i)}")

# Char: f --> ASCII Number: 102
# Char: a --> ASCII Number: 97
# Char: r --> ASCII Number: 114
# Char: a --> ASCII Number: 97
# Char: h --> ASCII Number: 104

ascii_codes = [71, 80, 100, 1, 0]

for j in ascii_codes:
    print(f"Ascii Number: {j} --> Char: {chr(j)}")

# Ascii Number: 71 --> Char: G
# Ascii Number: 80 --> Char: P
# Ascii Number: 100 --> Char: d
# Ascii Number: 1 --> Char: ☺
# Ascii Number: 0 --> Char:
