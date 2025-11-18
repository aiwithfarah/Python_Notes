# 1. declare variables and ds first
# 2. now write your functions
import random
from word_list import words

# display ascii art -->dict(key, tuple)
# key represents incorrect number of guesses | once we hit 6 incorrect guesses we loose the game

hangman_art = {0: ("   ",
               "   ",
                   "   "),
               1: (" O ",
               "   ",
                   "   "),
               2: (" O ",
               " | ",
                   "   "),
               3: (" O ",
               "/| ",
                   "   "),
               4: (" O ",
               "/|\\",
                   "   "),
               5: (" O ",
               "/|\\",
                   "/  "),
               6: (" O ",
               "/|\\",
                   "/ \\")}

# for line in hangman_art[6]:
#     print(line)


def display_man(wrong_guesses):

    print("*********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*********")


def display_hint(hint):  # hint is goign to be a list of _ characters. For each letter we guess right, we will flip each of those _ to a letter
    print(" ".join(hint))


# displays the correct answer either when we loose the game or win the game
def display_answer(answer):
    print("".join(answer))


def main():
    answer = random.choice(words)
    print(answer)

    hint = ['_'] * len(answer)
    print(hint)

    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        # to make sure user types in only one word
        if len(guess) != 1 or guess.isdigit():
            print("Invalid Input")
            continue
        # if a user types in a letter we've already guesses
        if guess in guessed_letters:
            print(f"You've already guessed the letter {guess}")
            continue  # to skip current loop iteration

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!!!!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Loose!")
            is_running = False


if __name__ == '__main__':  # if we are running this file directly call the main function to run the program
    main()
