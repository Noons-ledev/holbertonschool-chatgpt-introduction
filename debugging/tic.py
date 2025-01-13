def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner on the board.

    Returns True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the game has ended in a draw (i.e., all spots filled and no winner).
    
    Returns True if it's a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Runs the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]  # Initialize the board
    player = "X"  # Player X starts the game
    while True:
        print_board(board)  # Display the current board
        # Get row and column input from the player
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Check if the row and column are within the valid range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter values between 0 and 2.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player  # Make the move
            else:
                print("That spot is already taken! Try again.")
                continue
            
            # Check if there is a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            # Check for a draw condition
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch players
            player = "O" if player == "X" else "X"
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except IndexError:
            print("Invalid row or column. Please enter values between 0 and 2.")

# Start the game
tic_tac_toe()
