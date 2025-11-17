import random

# tuple since we are not going to be changing these options
options = ("rock", "paper", "scissors")

playing = True

while playing:
    player_choice = None
    computer_choice = random.choice(options)

    while player_choice not in options:
        player_choice = input(
            "Enter a choice between - 'rock', 'paper', 'scissors' ").lower()

    print(f"Player Choice: {player_choice}")
    print(f"Computer's Choice: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a Tie")
    elif player_choice == 'rock' and computer_choice == 'paper':
        print("You Win!")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('You Win!')
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('You Win!')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('You Win!')
    else:
        print("You Loose :(")

    if not input("Play again? (y/n): ").lower() == 'y':
        playing = False

print("Thanx for Playing!")
