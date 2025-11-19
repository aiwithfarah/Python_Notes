# Vowel Counter: Write a function that takes a string and returns a dictionary with the count
# of each vowel (a, e, i, o, u).

def vowel_counter(str1):

    vowels = dict()
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    for char in str1.lower():
        if char in vowels_list:
            current_count = vowels.get(char, 0)
            vowels[char] = current_count + 1

    print(vowels)


vowel_counter("aaaaabeecdi")
