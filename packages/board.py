from termcolor import colored


class Square:
    rows_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def __init__(self, x, y):
        self.position = (x, y)
        index = self.rows_letters.index(x)
        board.board[index][y - 1] = self


class White(Square):
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
        if self.selected == False:
            return colored(chr(9675), "red")
        else:
            return colored(chr(9689), "red")

    def move(self):
        if self.queen == False:
            possible_moves = []
            row = Square.rows_letters[Square.rows_letters.index(self.x) - 1]
            index = Square.rows_letters.index(row)
            first_option = f"{row}{str(self.y - 1)}"
            second_option = f"{row}{str(self.y + 1)}"
            if self.y - 1 > 0 and isinstance(board.board[index][self.y - 2], UserPiece) == False:
                possible_moves.append(first_option)
            if self.y + 1 < 9 and isinstance(board.board[index][self.y], UserPiece) == False:
                possible_moves.append(second_option)
            if len(possible_moves) == 0:
                return False
            print("Possible moves:")
            print(*possible_moves, sep=", ")
            while True:
                choose_move = input("Choose square which you want to go: ").capitalize()
                if choose_move == first_option:
                    self.change_position(row, self.y - 1)
                elif choose_move == second_option:
                    self.change_position(row, self.y + 1)
                else:
                    print("You must choose one of the following moves.")
                    continue
                break
        else:
            possible_moves = []
            index = Square.rows_letters.index(self.x)
            y = self.y
            while index > 0 and y > 1:
                index -= 1 
                y -= 1
                possible_moves.append((Square.rows_letters[index], y))
            index = Square.rows_letters.index(self.x)
            y = self.y
            while index > 0 and y < 8:
                index -= 1
                y += 1
                possible_moves.append((Square.rows_letters[index], y))
            index = Square.rows_letters.index(self.x)
            y = self.y
            while index < 7 and y > 1:
                index += 1
                y -= 1
                possible_moves.append((Square.rows_letters[index], y))
            index = Square.rows_letters.index(self.x)
            y = self.y
            while index < 7 and y < 8:
                index += 1
                y += 1
                possible_moves.append((Square.rows_letters[index], y))
            
            print(possible_moves)
class ComputerPiece(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        computer_pieces.append(self)

    def __repr__(self):
        if self.selected == False:
            return colored(chr(9675), "yellow")
        else:
            return colored(chr(9689), "yellow")


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
                            ComputerPiece(Square.rows_letters[list_index], square_index)
                    else:
                        if square_index == 0:
                            UserPiece(Square.rows_letters[list_index], 8)
                        else:
                            UserPiece(Square.rows_letters[list_index], square_index)

user_pieces = []
computer_pieces = []
board = Board()
create_board()
create_pieces(board.board[0], False)
create_pieces(board.board[1], True)
create_pieces(board.board[2], False)
create_pieces(board.board[5], True)
create_pieces(board.board[6], False)
create_pieces(board.board[7], True) 
# dupa = ComputerPiece("E", 2)
# dupa = ComputerPiece("E", 4)
# dupa = ComputerPiece("D", 3)
test = UserPiece("D", 5)
test.queen = True


