# FizzBuzz: Print numbers from 1 to 50.
#  If a number is divisible by 3, print "Fizz". If divisible by 5, print "Buzz".
#  If divisible by both, print "FizzBuzz".

def fizzbuzz():

    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBizz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


x = fizzbuzz()
