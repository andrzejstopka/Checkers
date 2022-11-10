class Board:
    board = []
    position_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    def show(self):
        print("   ", 1, 2, 3, 4, 5, 6, 7, 8, sep=" ")
        print("    ---------------")
        for row in self.board:
            for element in row:
                element = f"{element}|"
            print(row.name + ": ", *row.row)

    def __getitem__(self, key):
        return self.board[self.position_dict[key]]

    def __setitem__(self, index, row, value):
        self.board[self.position_dict[index][row]] = value


class Row:
    def __init__(self, letter, row):
        self.name = letter
        self.row = row
        board.board.append(self)

    def __repr__(self):
        return f"{self.name}: {self.row}"

    def __getitem__(self, index):
        return self.row[index - 1]

    def __setitem__(self, index, value):
        self.row[index - 1] = value

    def __delitem__(self, index):
        del self.row[index - 1]


class Pawn:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        board[x][y] = self
           
    def __repr__(self):
        return self.name


class ComputerPawn(Pawn):
    name = "X"

    def __init__(self, x, y):
        super().__init__(x, y)
        computer.pawns.append(self)


class UserPawn(Pawn):
    name = "1"

    def __init__(self, x, y):
        super().__init__(x, y)
        user.pawns.append(self)
    
    def move(self):
        def get_keys_from_value(dict, v):
            for key, value in dict.items():
                value += 1
                if value == v:
                    return key
        row = get_keys_from_value(board.position_dict, board.position_dict[self.x])
        first_y = self.y - 1
        second_y = self.y + 1
        if self.must_eat():
            go = input("You have a \"must eat\". Type \"go\" to eat opponent's pawn")
            if go == "go":
                self.change_position(self.must_eat().x, self.must_eat().y)
        else:
            print(f"{row}{first_y} / {row}{second_y}")
            
        
    def change_position(self, x, y):
        self.x = x
        self.y = y
        board[x][y] = self
        
    
    def must_eat(self):
        if not any(board.position_dict[pawn.x] + 1 == board.position_dict[self.x] and (pawn.y - 1 == self.y or pawn.y + 1 == self.y) for pawn in computer.pawns):
            return False
        else:
            for pawn in computer.pawns:
                if board.position_dict[pawn.x] + 1 == board.position_dict[self.x] and (pawn.y - 1 == self.y or pawn.y +1 == self.y):
                    return pawn
################### OGARNĄĆ USUWANIE ########################

class User:
    pawns = []


class Computer:
    pawns = []


all_pawns = []
board = Board()
user = User()
computer = Computer()


def create_pawn(row, pawn_type, from_second):
    for number, _ in enumerate(row):
        if from_second == True:
            if number % 2 == 0 and number > 0:
                pawn_type(row.name, number)
        else:
            if number % 2 == 1:
                pawn_type(row.name, number)


a = Row("A", [0] * 8)
b = Row("B", [0] * 8)
c = Row("C", [0] * 8)
d = Row("D", [0] * 8)
e = Row("E", [0] * 8)
f = Row("F", [0] * 8)
g = Row("G", [0] * 8)
h = Row("H", [0] * 8)

create_pawn(a, ComputerPawn, False)
create_pawn(b, ComputerPawn, True)
create_pawn(c, ComputerPawn, False)
create_pawn(f, UserPawn, True)
create_pawn(g, UserPawn, False)
create_pawn(h, UserPawn, True)
dupa = ComputerPawn("E", 1)

