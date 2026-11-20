print("TIC-TAC-TOE")
print("You are X, Computer is O")

# Board
#board = ["  " for _ in range(9)]
board = [' '] * 9

# Display board
def display():
    print()
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print("----+---+-----")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print("----+---+-----")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check winner
def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# AI move
def ai_move():
    # First, try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'

            if check_winner("O"):
                return

            board[i] = ' '

    # Block player's winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'

            if check_winner("X"):
                board[i] = 'O'
                return

            board[i] = ' '

    # Take center
    if board[4] == ' ':
        board[4] = 'O'
        return

    # Take a corner
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            board[i] = 'O'
            return

    # Take any remaining position
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return


# Main game
while True:
    display()

    position = int(input("Enter a position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != ' ':
        print("Invalid move")
        continue

    board[position] = "X"

    if check_winner("X"):
        display()
        print("You Win!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    # AI Move
    ai_move()

    if check_winner("O"):
        display()
        print("Computer Wins!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break