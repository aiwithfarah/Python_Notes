# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

# For example:

# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as the letters "d", "o", or "g" don't appear in this order)
# Hints:

# you should use the two-argument variants of the pos() functions inside your code;
# don't worry about case sensitivity.
# #

def find_word(word, sequence):

    # convert word and sequence to lower case
    word = word.lower()
    sequence = sequence.lower()

    current_position = 0
    found_all = True

    for char in word:
        # 2. Search for the character starting from current_position
        # sequence.find(char, start) returns the index of the char or -1
        res = sequence.find(char, current_position)

        if res == -1:
            # Character not found in the remaining part of the string
            found_all = False
            break

        current_position = res + 1

    if found_all:
        print("Yes")
    else:
        print("No")


find_word("dog", "vcxzxduybfdsobywuefgas")  # Output: Yes
find_word("dog", "vcxzxdcybfdstbywuefsas")  # Output: No
find_word("donor", "Nabucodonosor")  # Yes
