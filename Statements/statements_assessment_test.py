# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
st_to_list = st.split()
new_list = []

for first_letter in st_to_list:
    if first_letter[0] == "s":
        new_list.append(first_letter)
print(new_list)  # ['start', 's', 'sentence']

# Use range() to print all the even numbers from 0 to 10.

for n in range(11):
    if n % 2 == 0:
        print(n)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
lst = [x for x in range(1, 50) if x % 3 == 0]
print(lst)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# Go through the string below and if the length of a word is even print "even!"
ist = 'Print every word in this sentence that has an even number of letters'
ist_to_list = ist.split()
print(ist_to_list)
for word in ist_to_list:
    if len(word) % 2 == 0:
        print(word)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Use List Comprehension to create a list of the first letters of every word in the string below:
pst = 'Create a list of the first letters of every word in this string'
pst_to_list = [word[0] for word in pst.split()]
print(pst_to_list)
