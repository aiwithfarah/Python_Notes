# Number Guessing Game: The computer picks a random number between 1 and 100.
# The user has to guess it. The computer gives hints like "Too High" or "Too Low" until the user gets it right.
import random


def number_guessing_game():

    computer_pick = random.randint(1, 100)
    print(computer_pick)

    still_playing = True

    while still_playing:

        try:
            user_guess = int(input("Enter a number between 1 and 100: "))

            if user_guess < 1 or user_guess > 100:
                print("You have selected a value that is not in the valid range")
                print("Please select a number between 1 and 100")
            elif user_guess < computer_pick:
                print("Too Low")
            elif user_guess > computer_pick:
                print("Too High")
            else:
                print("You have guessed the right number")
                still_playing = False
        except ValueError:
            print("Invalid Input. Enter a number: ")


number_guessing_game()
