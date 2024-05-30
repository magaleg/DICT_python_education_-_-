"""project dominoes"""


import random


class DominoGame:
    """Class to run the dominoes game.
    :param: stock, the list of all dominoes.
    :param: computer_pieces, the list of computer's dominoes.
    :param: player_pieces, the list of player's dominoes.
    :param: snake, list of the on-table dominoes
    :param: str, the current player (player or computer)
    """
    def __init__(self):
        """
        Initializes the game, generates some amount of dominoes, gives some to the players.
        """
        self.stock = self.generate_stock()
        self.snake = []
        self.current_player = "player"
        self.deal_pieces_until_double_six()

    def generate_stock(self):
        """
        Generates the full amount of dominoes for the game.

        :return: list (of all possible dominoes)
        """
        return [[i, j] for i in range(7) for j in range(i, 7)]

    def deal_pieces(self):
        """
        Deals 7 pieces per person, the rest is in the stock.

        :return: tuple (for the player and for the computer)
        """
        random.shuffle(self.stock)
        return [self.stock.pop() for _ in range(7)], [self.stock.pop() for _ in range(7)]

    def deal_pieces_until_double_six(self):
        """
        Keeps dealing pieces until one of the players has the [6, 6] piece.
        """
        while True:
            self.stock = self.generate_stock()
            self.computer_pieces, self.player_pieces = self.deal_pieces()
            if [6, 6] in self.computer_pieces:
                self.current_player = "player"
                self.snake.append([6, 6])
                self.computer_pieces.remove([6, 6])
                break
            elif [6, 6] in self.player_pieces:
                self.current_player = "computer"
                self.snake.append([6, 6])
                self.player_pieces.remove([6, 6])
                break
            else:
                self.stock.extend(self.computer_pieces + self.player_pieces)

    def is_legal_move(self, piece, end):
        """
        Checks if the move is legal.

        :param piece: list, the piece the player wants to place.
        :param end: str, the end of the snake (left or right, + or -)
        :return: bool (true is everything is fine, false is the move is illegal)
        """
        if not self.snake:
            return True
        if end == "left":
            return piece[1] == self.snake[0][0] or piece[0] == self.snake[0][0]
        elif end == "right":
            return piece[0] == self.snake[-1][1] or piece[1] == self.snake[-1][1]
        return False

    def add_piece_to_snake(self, piece, end):
        """
        Adds a piece to the snake.

        :param piece: list, the piece to add
        :param end: str, the end of the snake (- or +).
        """
        if not self.snake:
            self.snake.append(piece)
        elif end == "left":
            if piece[1] == self.snake[0][0]:
                self.snake.insert(0, piece)
            else:
                self.snake.insert(0, piece[::-1])
        elif end == "right":
            if piece[0] == self.snake[-1][1]:
                self.snake.append(piece)
            else:
                self.snake.append(piece[::-1])

    def count_numbers(self):
        """
        Counts the usages of each number in the snake.

        :return: list of usages of numbers from 0 to 6
        """
        counts = [0] * 7
        for piece in self.snake + self.computer_pieces:
            counts[piece[0]] += 1
            counts[piece[1]] += 1
        return counts

    def rate_pieces(self):
        """
        Gives some amounts of counts to each piece of computer's domino

        :return: the dict of computer's dominoes and their counts.
        """
        counts = self.count_numbers()
        return {tuple(piece): counts[piece[0]] + counts[piece[1]] for piece in self.computer_pieces}

    def computer_move(self):
        """
        Makes the move of the computer, using the best piece for the move.
        """
        ratings = self.rate_pieces()
        sorted_pieces = sorted(self.computer_pieces, key=lambda piece: ratings[tuple(piece)], reverse=True)
        for piece in sorted_pieces:
            if self.is_legal_move(piece, "left"):
                self.add_piece_to_snake(piece, "left")
                self.computer_pieces.remove(piece)
                return
            elif self.is_legal_move(piece, "right"):
                self.add_piece_to_snake(piece, "right")
                self.computer_pieces.remove(piece)
                return
        if self.stock:
            self.computer_pieces.append(self.stock.pop())

    def player_move(self, move):
        """
        Allows the player to make their move.

        :param move: int, the move of the player.
        :return: true if everything is fine, false if there's an error.
        """
        if move == 0:
            if self.stock:
                self.player_pieces.append(self.stock.pop())
        else:
            piece_index = abs(move) - 1
            if piece_index >= len(self.player_pieces):
                print("Invalid input. Please try again.")
                return False
            piece = self.player_pieces[piece_index]
            if move < 0:
                if not self.is_legal_move(piece, "left"):
                    print("Illegal move. Please try again.")
                    return False
                self.add_piece_to_snake(piece, "left")
            else:
                if not self.is_legal_move(piece, "right"):
                    print("Illegal move. Please try again.")
                    return False
                self.add_piece_to_snake(piece, "right")
            self.player_pieces.pop(piece_index)
        return True

    def check_game_end(self):
        """
        Checks if the game's ended.

        :return: bool (true if yes, false if no)
        """
        if not self.player_pieces:
            print("Status: The game is over. You won!")
            return True
        if not self.computer_pieces:
            print("Status: The game is over. The computer won!")
            return True
        if self.snake:
            left, right = self.snake[0][0], self.snake[-1][1]
            if left == right and sum(1 for piece in self.snake if left in piece) >= 8:
                print("Status: The game is over. It's a draw!")
                return True
        return False

    def display_game(self):
        """
        Shows the current state of the game.
        """
        if len(self.snake) > 6:
            snake_str = f"{self.snake[:3]}...{self.snake[-3:]}"
        else:
            snake_str = ''.join(str(piece) for piece in self.snake)

        print("=" * 60)
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.computer_pieces)}")
        print(snake_str)
        print("Your pieces:")
        for i, piece in enumerate(self.player_pieces):
            print(f"{i + 1}:{piece}")
        print(
            f"Status: {'It is your turn to make a move. Enter your command.' if self.current_player == 'player' else 'Computer is about to make a move. Press Enter to continue...'}")

    def play(self):
        """
        Runs the game, gives turns to player and computer until the game ends.
        """
        while True:
            self.display_game()
            if self.check_game_end():
                break
            if self.current_player == "player":
                move = input("> ")
                try:
                    move = int(move)
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
                if self.player_move(move):
                    self.current_player = "computer"
            else:
                input("> ")
                self.computer_move()
                self.current_player = "player"


if __name__ == "__main__":
    game = DominoGame()
    game.play()
