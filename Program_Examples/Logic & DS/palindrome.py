# Challenge 2: The Palindrome Hunter
# Write a function is_palindrome(text).
# It should return True if the text looks the same backward (e.g., "madam", "racecar") and False otherwise.
# Hint: Slicing [::-1] is your friend.

def palindrome_hunter(text):

    if text == text[::-1]:
        return True
    else:
        return False


x = palindrome_hunter('madam')
y = palindrome_hunter('racecar')
print(x)
print(y)
