# IN and NOT IN - used to test whether a value is found in a sequence

word = 'apple'

letter = input('guess a letter in the secret word: ').lower()

if letter in word:
    print(f"Letter {letter} is in the word!")
else:
    print(f"Letter {letter} is not in the word!")
