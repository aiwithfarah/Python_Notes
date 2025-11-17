import random

lowest_num = 1
highest_num = 100

random_number = random.randint(lowest_num, highest_num)
print(random_number)

guesses = 0
is_running = True


while is_running:
    user_guess = input(">>>Enter a number between 1 & 101: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
        if user_guess < lowest_num or user_guess > highest_num:
            print(
                f"Number out of range. Please select a number between {lowest_num} and {highest_num}")
            print("Enter a number between 1 and 101: ")
        elif user_guess < random_number:
            print("Too low. Try again!!")
        elif user_guess > random_number:
            print("Too High. Try again!")

        else:
            print(f"You are correct.{random_number} is the Answer.")
            print(f"Number of guesses {guesses}")
            is_running = False
    else:
        print("Invalid Guess. ")
        print(f"Please select a number between {lowest_num} and {highest_num}")
