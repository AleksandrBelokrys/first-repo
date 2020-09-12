from string import ascii_uppercase

from chess import Pawn, Queen


class Board(object):

    def __init__(self, max_width=8, max_height=8):
        self.max_width = max_width
        self.max_height = max_height

        self.board = [[None] * self.max_width for i in range(self.max_height)]



    def _conv_position(self, position: str) -> list:

        if len(position) != 2:
            raise ValueError("The position must contain 2 characters!")

        width = str(position[0])
        if width not in ascii_uppercase:
            raise ValueError("The first character must be an uppercase letter")

        height = int(position[1])
        width = ascii_uppercase.index(width)
        height -= 1
        return [width, height]


    def get_piece(self, position: str):
        width, height = self._conv_position(position)

        if self.board[width][height]:
            return self.board[width][height]
        else:
            raise ValueError("There is no chess piece in this position!")



    def add_piece(self, piece, position: str):
        width, height = self._conv_position(position)

        if self.board[width][height]:
            raise ValueError("There is already a chess piece in this position!")

        self.board[width][height] = piece




    def remowe_piece(self, position: str) -> None:
        width, height = self._conv_position(position)

        if self.board[width][height]:
            self.board[width][height] = None
        else:
            raise ValueError("There is no chess piece in this position!")













my_board = Board(8, 8)

pawn1 = Pawn("while", "A1")
pawn2 = Pawn("black", "B2")
queen1 = Queen("while", "C1")

my_board.add_piece(queen1, "C1")

my_board.add_piece(pawn1, "A1")
my_board.add_piece(pawn2, "B2")







