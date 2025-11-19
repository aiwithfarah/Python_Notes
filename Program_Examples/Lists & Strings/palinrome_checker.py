# Palindrome Checker: Ask the user for a word and check if it reads the same backwards
# and forwards (ignoring case).

def palindrome(str1):

    lower_str = str1.lower().replace(" ", "")
    if lower_str == lower_str[::-1]:
        return "Is Palindrome"
    else:
        return "Is not Palindrome"


x = palindrome("nurses run")
print(x)
