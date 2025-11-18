# Write a function that computes the volume of a sphere given its radius.

import string


def vol_of_sphere(radius):
    return (4/3 * 3.14 * radius**3)


x = vol_of_sphere(2)
print(x)  # 33.49333333333333


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def find_num(num, low, high):

    if num in range(low, high+1):
        return f"{num} is in the range between {low} and {high}"


y = find_num(5, 2, 7)
print(y)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.


def calc_upper_lower(test_string):

    print(len(test_string))
    lower_count = 0
    upper_count = 0

    for letter in test_string:
        if letter.isupper():
            upper_count += 1
        else:
            lower_count += 1

    print(f"No of upper case letter {upper_count}")
    print(f"No of lower case letter {lower_count}")


calc_upper_lower("Hello Mr. Rogers, how are you this fine Tuesday?")

# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_elements(num_list):

    new_list = []
    for _ in num_list:
        if _ not in new_list:
            new_list.append(_)
    return new_list


x = unique_elements([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
print(x)  # [1,2,3,4,5]

# Write a Python function to multiply all the numbers in a list.


def multiply(n_list):

    multuplication_sum = 1
    for _ in n_list:
        multuplication_sum *= _
        # print(multuplication_sum)
    return multuplication_sum


x = multiply([1, 2, 3, -4])
print(x)

# Write a Python function that checks whether a word or phrase is palindrome or not.A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar


def palindrome(given_string):

    s = given_string.replace(" ", "")
    return s == s[::-1]


x = palindrome("racecar")
print(x)


# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
def check_panagram(str1):

    alphabet = string.ascii_lowercase
    alphaset = set(alphabet)
    print(alphaset)

    str1.replace(" ", "")
    # print(str1)
    str1 = str1.lower()
    # print(str1)

    for letter in alphaset:
        if letter not in str1:
            return False
    else:
        return True


x = check_panagram("The quick brown fox jumps over the lazy dog")
print(x)
