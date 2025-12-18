def check_sudoku():
    board = []

    print("Enter the 9 rows od Sudoku")
    for i in range(9):
        row_string = input()

        # check if input is exactly 9 digits
        if len(row_string) != 9 or not row_string.isdigit():
            print("Invalud Data")
            return

        # convert string 123 to list [1,2,3]
        row = [int(digit) for digit in row_string]
        board.append(row)

# helper func to check of the list of 9 numbers contaisn all 9 numebrs

    def is_valid_group(group):
        return sorted(group) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. Check Rows
    for row in board:
        if not is_valid_group(row):
            print("No")
            return

    # 3. Check Columns
    # We construct each column by taking the ith element from every row
    for col_index in range(9):
        column = []
        for row in board:
            column.append(row[col_index])

        if not is_valid_group(column):
            print("No")
            return

    # 4. Check 3x3 Sub-squares
    # We jump by 3 (0, 3, 6) to find the top-left corner of each block
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = []
            # Gather the 9 cells for this block
            for i in range(3):
                for j in range(3):
                    square.append(board[r + i][c + j])

            if not is_valid_group(square):
                print("No")
                return

    # If we passed all checks
    print("Yes")


# Run the program
check_sudoku()
