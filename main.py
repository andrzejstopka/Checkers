from packages.board import *


def must_eat():
    result = {}
    for user_piece in user_pieces:
        next_row = Square.rows_letters[Square.rows_letters.index(user_piece.x) - 2]
        row = Square.rows_letters[Square.rows_letters.index(user_piece.x) - 1]
        first_y = user_piece.y - 1
        second_y = user_piece.y + 1
        for computer_piece in computer_pieces:
            index = Square.rows_letters.index(next_row)
            if user_piece in result and (computer_piece.position == (row, first_y) or computer_piece.position == (row, second_y)):
                result[user_piece] = result[user_piece], computer_piece
            elif computer_piece.position == (row, first_y) and isinstance(board.board[index][first_y - 2], White):
                result[user_piece] = computer_piece
            elif computer_piece.position == (row, second_y) and isinstance(board.board[index][first_y + 2], White):
                result[user_piece] = computer_piece
    if len(result) == 0:
        return False
    print("You have the must eat! Choose a piece: ")
    for key in result.keys():
        print(f"{key.x}{key.y}", sep=" ", end=" ")
    print("\r")
    select_piece = input("Select a piece: ").capitalize()
    for piece, square in result.items():
        next_row = Square.rows_letters[Square.rows_letters.index(piece.x) - 2]
        if select_piece == f"{piece.x}{str(piece.y)}":
            if isinstance(square, Piece):
                piece.selected = True
                board.display()
                if piece.y > square.position[1]:
                    piece.change_position(next_row, square.position[1] - 1)
                else:
                    piece.change_position(next_row, square.position[1] + 1)
                piece.selected = False
                White(square.position[0], square.position[1])
                computer_pieces.remove(square)
            elif isinstance(square, tuple):
                for option in square:
                    print(f"{option.x}{option.y}", sep=" ", end=" ")
                print("\r")
                select_piece_to_eat = input("Choose a piece to eat: ").capitalize()
                for option in square:
                    if select_piece_to_eat == f"{option.x}{str(option.y)}":
                        piece.selected = True
                        board.display()
                        if piece.y > option.y:
                            piece.change_position(next_row, option.y - 1)
                        else:
                            piece.change_position(next_row, option.y + 1)
                        piece.selected = False
                        White(option.x, option.y)
                        computer_pieces.remove(option)                                              
    return True

def user_turn():
    while True:
        try:
            select_piece = input("Select a piece's row [\"A\"-\"H\"] and row [1-8]: ")
            select_piece_x = select_piece[0].capitalize()
            select_piece_y = int(select_piece[1])
            if all(piece.position != (select_piece_x, select_piece_y) for piece in user_pieces):
                raise ValueError
        except ValueError:
            print("There is no such piece, try again.")
            continue
        break
    for piece in user_pieces:
        if piece.position == (select_piece_x, select_piece_y):
            piece.selected = True
            board.display()
            if piece.move() == False:
                print("The piece can't be moved")
                piece.selected = False
                return False
            piece.selected = False
            

while True:
    board.display()
    if must_eat() == True:
        continue
    user_turn()
    
    
        
    