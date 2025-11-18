# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_evens(num1, num2):

    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
    else:
        if num1 > num2:
            return num1
        else:
            return num2


x = lesser_of_evens(2, 4)
y = lesser_of_evens(2, 5)
print(x)
print(y)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter


def two_word_str(str1):

    split_string = str1.split()
    # print(split_string)
    if split_string[0][0] == split_string[1][0]:
        return True
    else:
        return False


x = two_word_str("Levelheaded Llama")
print(x)

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
#  If not, return False


def makes_twenty(num1, num2):
    if num1+num2 == 20 or num1 == 20 or num2 == 20:
        return True
    else:
        return False


ans_1 = makes_twenty(20, 10)
ans_2 = makes_twenty(13, 12)
print(ans_1)  # True
print(ans_2)  # False

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# macdonald


def old_macdonald(str1):
    first_letter = str1[0].upper()
    fourth_letter = str1[3].upper()
    if len(str1) > 3:
        return first_letter + str1[1:3] + fourth_letter + str1[4:]
    else:
        return "Lenght is too short!"


answ = old_macdonald("macdonald")
print(answ)

# MASTER YODA: Given a sentence, return a sentence with the words reversed


def words_reversed(str1):
    split_str = str1.split()
    print(split_str)
    reversed_list = split_str[::-1]
    new_string = ""
    for word in reversed_list:
        new_string += word + " "
    return new_string


x = words_reversed("I am home")
print(x)


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def within_10(n):

    if ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)):
        return True
    else:
        return False


x = within_10(110)
print(x)

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.


def has_33(num_list):

    for i in range(0, len(num_list)-1):
        if num_list[i] == 3 and num_list[i+1] == 3:
            return True
    else:
        return False


x = has_33([1, 3, 3])
y = has_33([1, 3, 1, 3])
z = has_33([3, 1, 3])
print(x)
print(y)
print(z)

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def paper_doll(str1):

    new_str = ''
    for letter in str1:
        new_str += letter*3
    return new_str


x = paper_doll('Hello')
y = paper_doll('Mississippi')
print(x)
print(y)


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
#  return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def black_jack(n1, n2, n3):

    summation = n1+n2+n3
    if summation <= 21:
        return summation
    elif summation > 21 and 11 in (n1, n2, n3):
        return summation-10
    else:
        return "Bust"


x = black_jack(5, 6, 7)
y = black_jack(9, 9, 9)
z = black_jack(9, 9, 11)
print(x)
print(y)
print(z)


# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(num_list):

    total = 0
    ignoring = False

    for num in num_list:
        if num == 6:
            ignoring = True
        elif num == 9:
            ignoring = False

        elif ignoring == False:
            total += num
    return total


x = summer_69([1, 3, 5])
y = summer_69([4, 5, 6, 7, 8, 9])
z = summer_69([2, 1, 6, 9, 11])
print(x)
print(y)
print(z)


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(num_list):

    for num in range(0, len(num_list) - 1):
        if num_list[num] == 0 and num_list[num + 1] == 0 and num_list[num + 2] == 7:
            return True
    else:
        return False


x = spy_game([1, 2, 4, 0, 0, 7, 5])
y = spy_game([1, 0, 2, 4, 0, 5, 7])
z = spy_game([1, 7, 2, 0, 4, 5, 0])
print(x)
print(y)
print(z)

# COUNT PRIMES: Write a function that returns the number of prime numbers
# that exist up to and including a given number


def count_primes(num):

    prime_count = 0

    if num < 2:
        return 0
    for n in range(2, num+1):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
    return prime_count


x = count_primes(100)
print(x)
