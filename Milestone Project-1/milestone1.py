import random
import os


def clear_screen():
    """Clears the console screen."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        os.system('clear')


def display_board(board):
    """
    Prints the Tic-Tac-Toe board.
    """
    clear_screen()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    """
    Asks Player 1 to choose 'X' or 'O' and returns
    a tuple (Player 1 marker, Player 2 marker).
    """
    marker = ''

    # Keep asking Player 1 to choose 'X' or 'O'
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    """
    Places the given marker ('X' or 'O') on the board
    at the given position (1-9).
    """
    board[position] = marker


def win_check(board, mark):
    """
    Checks if a player has won the game.
    """
    # Check all rows
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across top
            # across middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or

            # Check all columns
            # down left
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down right
            (board[9] == mark and board[6] == mark and board[3] == mark) or

            # Check diagonals
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    """
    Randomly selects which player goes first.
    """
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    """
    Checks if a space on the board is free.
    Returns True if the space is ' '.
    """
    return board[position] == ' '


def full_board_check(board):
    """
    Checks if the board is full.
    Returns True if full, False otherwise.
    """
    # Loop from 1 to 9
    for i in range(1, 10):
        if space_check(board, i):
            # Found a free space, board is not full
            return False
    # No free spaces found, board is full
    return True


def player_choice(board):
    """
    Asks the player for their next position (1-9)
    and checks if it's a valid, free space.
    """
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        try:
            position_input = input('Choose your next position (1-9): ')
            position = int(position_input)

            if position not in range(1, 10):
                print("Invalid input. Please choose a number between 1 and 9.")
            elif not space_check(board, position):
                print("That space is already taken!")

        except ValueError:
            print("Invalid input. Please enter a number.")

    return position


def replay():
    """
    Asks the players if they want to play again.
    Returns True if they do, False if they don't.
    """
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# --- Main Game Logic ---


print('Welcome to Tic Tac Toe!')

while True:
    # --- Game Setup ---
    # Create a new, empty board
    # We use 10 items and ignore index 0 for easy 1-9 mapping
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    game_on = True

    # --- Single Game Loop ---
    while game_on:
        if turn == 'Player 1':
            # --- Player 1's Turn ---

            # 1. Display the board
            display_board(theBoard)
            # 2. Get the player's choice
            position = player_choice(theBoard)
            # 3. Place the marker
            place_marker(theBoard, player1_marker, position)

            # 4. Check for a win
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 has won!')
                game_on = False
            # 5. Check for a tie
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                game_on = False
            # 6. Switch turns
            else:
                turn = 'Player 2'

        else:
            # --- Player 2's Turn ---

            # 1. Display the board
            display_board(theBoard)
            # 2. Get the player's choice
            position = player_choice(theBoard)
            # 3. Place the marker
            place_marker(theBoard, player2_marker, position)

            # 4. Check for a win
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 has won!')
                game_on = False
            # 5. Check for a tie
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                game_on = False
            # 6. Switch turns
            else:
                turn = 'Player 1'

    # --- End of Single Game ---

    # Ask to play again. If replay() returns False, break the loop.
    if not replay():
        break

print('Thanks for playing!')
