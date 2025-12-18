def is_anagram():
    # 1. Get input from the user
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    # 2. Rule: Empty strings are not anagrams
    if not text1.strip() or not text2.strip():
        print("Not anagrams")
        return

    # 3. Clean the strings:
    # - Remove spaces using replace(" ", "")
    # - Convert to lowercase using lower()
    clean1 = text1.replace(" ", "").lower()
    clean2 = text2.replace(" ", "").lower()

    # 4. Sort the characters and compare
    # sorted() returns a list of characters in alphabetical order
    if sorted(clean1) == sorted(clean2):
        print("Anagrams")
    else:
        print("Not anagrams")


# Run the function
is_anagram()
