# It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

# Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

# Each digit is constructed from 13 LEDs (some lit, some dark, of course) – that's how we imagine it:

# Each list represents rows 1 through 5 for that specific digit
digits = {
    '0': ["###", "# #", "# #", "# #", "###"],
    '1': ["  #", "  #", "  #", "  #", "  #"],
    '2': ["###", "  #", "###", "#  ", "###"],
    '3': ["###", "  #", "###", "  #", "###"],
    '4': ["# #", "# #", "###", "  #", "  #"],
    '5': ["###", "#  ", "###", "  #", "###"],
    '6': ["###", "#  ", "###", "# #", "###"],
    '7': ["###", "  #", "  #", "  #", "  #"],
    '8': ["###", "# #", "###", "# #", "###"],
    '9': ["###", "# #", "###", "  #", "###"]
}


def ledDisplay(number):

    # convert num to string to iterate through digits
    str_num = str(number)

    # We need to loop 5 times because every digit is 5 rows high
    for row in range(5):
        line = ""
        for char in str_num:
            if char in digits:
                # Add the specific row of the current digit plus a space for padding
                line += digits[char][row] + " "

        print(line)


# Example Usage:
user_input = input("Enter a non-negative integer: ")
ledDisplay(user_input)
