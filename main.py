from packages.board import *


def must_eat():
    result = {}
    for user_piece in user_pieces:
        row = Square.rows_letters[Square.rows_letters.index(user_piece.x) - 1]
        first_y = user_piece.y - 1
        second_y = user_piece.y + 1
        for computer_piece in computer_pieces:
            if user_piece in result and (computer_piece.position == (row, first_y) or computer_piece.position == (row, second_y)):
                result[user_piece] = result[user_piece], computer_piece
            elif computer_piece.position == (row, first_y):
                result[user_piece] = computer_piece
            elif computer_piece.position == (row, second_y):
                result[user_piece] = computer_piece
    if len(result) == 0:
        return False
    
    print("You have the must eat! Choose a piece: ")
    for key in result.keys():
        print(f"{key.x}{key.y}", end=" ")
    print("\r")
    select_piece = input("Select a piece: ")
    for piece, square in result.items():
        if select_piece == f"{piece.x}{str(piece.y)}":
            if isinstance(square, Piece):
                piece.selected = True
                board.display()
                piece.change_position(square.position[0], square.position[1])
                piece.selected = False
                computer_pieces.remove(square)
            else:
                for option in square:
                    print(f"{option.x}{option.y}", end=" ")
                print("\r")
                select_piece_to_eat = input("Choose a piece to eat: ")
                for option in square:
                    if select_piece_to_eat == f"{option.x}{str(option.y)}":
                        piece.selected = True
                        board.display()
                        piece.change_position(option.x, option.y)
                        piece.selected = False
                        computer_pieces.remove(option)
    return True

def user_turn():
    select_piece_x = input("Select pieces's row [\"A\"-\"H\"]: ")
    select_piece_y = int(input("Select pieces's column [1-8]: "))
    for piece in user_pieces:
        if piece.position == (select_piece_x, select_piece_y):
            piece.selected = True
            board.display()
            piece.move()
            piece.selected = False
    

while True:
    board.display()
    if must_eat() == True:
        continue
    user_turn()