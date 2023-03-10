from termcolor import colored

computer_pieces = []
user_pieces = []
white_squares = []


class Square:
    rows_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (x, y)
        index = self.rows_letters.index(x)
        board.board[index][y - 1] = self


class White(Square):
    def __init__(self, x, y):
        super().__init__(x, y)
        white_squares.append(self)

    def __repr__(self):
        return chr(9632)


class Blue(Square):
    def __repr__(self):
        return colored(chr(9632), "blue")


class Board:
    def display(self):
        print("   ", 1, 2, 3, 4, 5, 6, 7, 8, sep=" ")
        i = 0
        for x in self.board:
            print(Square.rows_letters[i] + ": ", *x)
            i += 1

    def __init__(self):
        self.board = [[0]*8 for i in range(8)]


class Piece:

    selected = False
    queen = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (x, y)
        index = Square.rows_letters.index(x)
        board.board[index][y - 1] = self

    def change_position(self, x, y):
        if x == "A":
            self.queen = True
        index = Square.rows_letters.index(self.x)
        board.board[index][self.y - 1] = White(self.x, self.y)
        self.x = x
        self.y = y
        self.position = (x, y)
        index = Square.rows_letters.index(x)
        board.board[index][y - 1] = self


class UserPiece(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        user_pieces.append(self)

    def __repr__(self):
        if self.queen == False:
            if self.selected == False:
                return colored(chr(9675), "red")
            else:
                return colored(chr(9689), "red")
        else:
            return colored(chr(9830), "red")

class ComputerPiece(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        computer_pieces.append(self)

    def __repr__(self):
        if self.queen == False:
            if self.selected == False:
                return colored(chr(9675), "yellow")
            else:
                return colored(chr(9689), "yellow")
        else:
            return colored(chr(9830), "yellow")
               
    
def create_board():
    i = 0
    for row in board.board:
        n = 1
        for square in row:
            if (i % 2 == 0 and n % 2 == 1) or (i % 2 == 1 and n % 2 == 0):
                Blue(Square.rows_letters[i], n)
            else:
                White(Square.rows_letters[i], n)
            n += 1
        i += 1


def create_pieces(row, from_second):
    list_index = board.board.index(row)
    if list_index in [0, 1, 2, 5, 6, 7]:
        if from_second == True:
            for square in row:
                square_index = row.index(square)
                if square_index in [1, 3, 5, 7]:
                    if list_index < 3:
                        ComputerPiece(
                            Square.rows_letters[list_index], square_index)
                    else:
                        UserPiece(
                            Square.rows_letters[list_index], square_index)
        else:
            for square in row:
                square_index = row.index(square)
                if square_index in [0, 2, 4, 6]:
                    if list_index < 3:
                        if square_index == 0:
                            ComputerPiece(Square.rows_letters[list_index], 8)
                        else:
                            ComputerPiece(
                                Square.rows_letters[list_index], square_index)
                    else:
                        if square_index == 0:
                            UserPiece(Square.rows_letters[list_index], 8)
                        else:
                            UserPiece(
                                Square.rows_letters[list_index], square_index)


board = Board()
create_board()
create_pieces(board.board[0], False)
create_pieces(board.board[1], True)
create_pieces(board.board[2], False)
create_pieces(board.board[5], True)
create_pieces(board.board[6], False)
create_pieces(board.board[7], True)


for x in white_squares:
    if x.position[0] == "A" or x.position[0] == "B" or x.position[0] == "C" or x.position[0] == "F" or x.position[0] == "G" or x.position[0] == "H":
        white_squares.remove(x)
for x in white_squares:
    if x.position[0] == "A" or x.position[0] == "B" or x.position[0] == "C" or x.position[0] == "F" or x.position[0] == "G" or x.position[0] == "H":
        white_squares.remove(x)
for x in white_squares:
    if x.position[0] == "A" or x.position[0] == "B" or x.position[0] == "C" or x.position[0] == "F" or x.position[0] == "G" or x.position[0] == "H":
        white_squares.remove(x)

for x in white_squares:
    if x.position[0] == "A" or x.position[0] == "B" or x.position[0] == "C" or x.position[0] == "F" or x.position[0] == "G" or x.position[0] == "H":
        white_squares.remove(x)


