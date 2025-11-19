# Morse Code Translator: Create a dictionary that maps letters to Morse code (e.g., 'A': '.-').
#  Write a program that translates a user's input string into Morse code.

def morse_code_translator(code):

    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/'  # We use a slash to represent a space between words


    }

    translated_text = ""
    code = code.upper()
    for char in code:
        if char in morse_code_dict:
            translated_text += morse_code_dict[char] + " "

    return translated_text


x = morse_code_translator("SOS")
y = morse_code_translator("HELLO")
z = morse_code_translator("123")
print(x)
print(y)
print(z)
