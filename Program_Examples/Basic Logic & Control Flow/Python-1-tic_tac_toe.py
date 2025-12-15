import random
from random import randrange


def display_board(board):
    print("+------" * 3 + "+")
    for row in range(3):
        print("|      " * 3 + "|")
        for col in range(3):
            print("|  " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|      " * 3 + "|")
        print("+------" * 3 + "+")


def enter_move(board):
    ok = False
    while not ok:
        user_move = input("Enter your move: ")
        # check if use input is valid
        ok = len(user_move) == 1 and user_move >= '1' and user_move <= '9'
        if not ok:
            print("Incorrect Move. Try Again!>>>")
            continue

        # update board accordin to user's decision
        user_move = int(user_move) - 1
        row = user_move // 3  # cells' row
        col = user_move % 3  # cell's column
        sign = board[row][col]  # mark the selected square

        if sign in ['X', 'O']:
            print("This filed is already occupied! Repeat Input")
            ok = False
            continue
    board[row][col] = "O"  # set O at the selected cell


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    # check rows
    for r in range(3):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True

    # check columns
    for c in range(3):
        if board[c][0] == sign and board[c][1] == sign and board[c][2] == sign:
            return True

    # check diagonally
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    print("Computer makign move.....")
    free = make_list_of_free_fields(board)  # make list of free fields
    count = len(free)
    if count > 0:
        # computer chooses random index from free list
        this = randrange(count)
        row, col = free[this]
        board[row][col] = 'X'

        # initialize the board - comp starts with x in the middle
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

human_turn = True

while True:
    display_board(board)
    if human_turn:
        enter_move(board)
        victory = victory_for(board, 'O')
    else:
        draw_move(board)
        victory = victory_for(board, 'X')

    if victory:
        display_board(board)
        if human_turn:
            print("You won!")
        else:
            print("The computer won!")
        break

    human_turn = not human_turn

    # Check for Tie
    # If the list of free fields is empty and no one won, it's a tie
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Game over! It's a tie!")
        break
