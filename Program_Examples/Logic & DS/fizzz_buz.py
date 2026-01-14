# Write a function fizzbuzz(n) that loops from 1 to n.
# If a number is divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both (like 15), print "FizzBuzz".
# Otherwise, print the number.

def fizzBuzz(num):

    for n in range(num):
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif (n % 3 == 0):
            print("Fizz")
        elif (n % 5 == 0):
            print("Buzz")
        else:
            print(n)


x = fizzBuzz(40)
print(x)
