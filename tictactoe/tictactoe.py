"""Project Tictactoe"""


def print_board(board):
    """
    A function that creates a board for the game by placing symbols and empty spaces for each row.
    Prints horizontal boards using - and vertical using |.
    Basically creates a list out of lists, in which each list is a row of the board.

    :param board: List.
    :return: None.
    """
    print("---------")
    for row in board:
        print("|", " ".join(row), "|")
    print("---------")


def is_valid_coordinates(coordinates, board):
    """
    This function checks if the inputted coordinates are valid.
    It checks if they are in between 1 and 3 or if the coordinates are still free,
    then returns True if yes, False if no.

    :param coordinates: Tuple, includes x and y (row and column)
    :param board: list that is used to create a board
    :return: Bool:  True if successful,
                    False if the cell is already occupied or the coordinates are wrong.
    """
    x, y = coordinates
    if not (1 <= x <= 3 and 1 <= y <= 3):
        print("Coordinates should be from 1 to 3!")
        return False
    elif board[x - 1][y - 1] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    return True


def get_user_coordinates():
    """
    This function lets user input their coordinates, then checks if they're valid
    (if there are two of them + if they are numbers) and uses map to read all
    the elements of coordinates list and put them into tuple.

    :return: if everything is fine, returns Tuple with coordinates (row and column)
    """
    while True:
        try:
            coordinates = input("Enter your coordinates!> ").split()
            coordinates = tuple(map(int, coordinates))
            if len(coordinates) == 2:
                return coordinates
            else:
                print("You should enter exactly two numbers!")
        except ValueError:
            print("No, you should enter numbers!")


def analyze_board(board):
    """ An important function that analyzes the board.
    Copies rows from the board, then creates a list for columns by reading board and choosing right elements,
    then creates diagonals.
    Then creates list of lines, then checks if there's a line of Xs or Os

    :param: board (list)
    :return: str:   "Congrats, X wins!" if X wins,
                    "Congrats, O wins!" if O wins,
                    "It's a draw!" if it's a draw between X and O
                    "Game not finished" if not each of those
    """
    rows = board
    columns = [[board[j][i] for j in range(3)] for i in range(3)]
    diagonals = [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]

    lines = rows + columns + diagonals

    x_wins = any(line.count("X") == 3 for line in lines)
    o_wins = any(line.count("O") == 3 for line in lines)

    if x_wins:
        return "Congrats, X wins!"
    elif o_wins:
        return "Congrats, O wins!"
    elif " " not in [cell for row in board for cell in row]:
        return "It's a draw!"
    else:
        return "Game not finished"


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


while True:
    # Not a function, but the main cycle of the game. Prints the board.
    print_board(board)

    while True:
        """Cycle that uses function to get the coordinates from the user, user another one to check them, then places
        X in the right place and breaks."""
        coordinates = get_user_coordinates()
        if is_valid_coordinates(coordinates, board):
            x, y = coordinates
            board[x - 1][y - 1] = "X"
            break

    result = analyze_board(board)
    if result != "Game not finished":
        print_board(board)
        print(result)
        break

    print_board(board)

    while True:
        """The same for O."""
        coordinates = get_user_coordinates()
        if is_valid_coordinates(coordinates, board):
            x, y = coordinates
            board[x - 1][y - 1] = "O"
            break

    result = analyze_board(board)
    if result != "Game not finished":
        print_board(board)
        print(result)
        break

