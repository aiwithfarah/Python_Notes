from random import shuffle

# InitialList
my_list = ["", "O", ""]

# Shuffle List
shuffle(my_list)
print(my_list)


# USer Guess
def player_guess():

    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input(">>>Pick a number: ")
    return int(guess)


x = player_guess()
print(x)

# Check Guess


def check_guess(my_list, guess):
    if my_list[guess] == "O":
        print("Correct Guess")
    else:
        print("Wrong Guess")


check_guess(my_list, x)
