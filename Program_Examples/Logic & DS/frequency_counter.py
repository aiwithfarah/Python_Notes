# Challenge 3: The Frequency Counter
# Input: A list votes = ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Blue'].
# Task: Write a function that counts the votes using a Dictionary and returns it.
# Expected Output: {'Red': 2, 'Blue': 3, 'Green': 1}.

def frequencyCounter(lst):

    dict_counter = {}

    for color in lst:
        if color in dict_counter:
            dict_counter[color] = dict_counter[color] + 1
        else:
            dict_counter[color] = 1
    print(dict_counter)


x = frequencyCounter(['Red', 'Blue', 'Red', 'Green', 'Blue', 'Blue'])
