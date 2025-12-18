text = input("Enter the text to be checked: ").lower()
lowertext_without_space = text.replace(" ", "")

print(text[::-1])
if text[::-1].replace(" ", "") == lowertext_without_space:
    print("Palindrome")
else:
    print("Not a Palindrome")
