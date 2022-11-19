from packages.board import *


def possible_eating(piece, opponent_pieces):
    possible_eating = []
    piece_row_index = Square.rows_letters.index(piece.x)
    if piece.queen == False:
        for opponent_piece in opponent_pieces:
            opponent_piece_row_index = Square.rows_letters.index(opponent_piece.x)
            rows_difference1 = piece_row_index + 1 == opponent_piece_row_index or piece_row_index - 1 == opponent_piece_row_index
            column_difference1 = piece.y - 1 == opponent_piece.y or piece.y + 1 == opponent_piece.y
            if rows_difference1 == True and column_difference1 == True:
                for square in white_squares:
                    square_row_index = Square.rows_letters.index(square.x)
                    if piece.x > opponent_piece.x and piece.y < opponent_piece.y:
                        if opponent_piece_row_index - 1 == square_row_index and opponent_piece.y + 1 == square.y:
                            possible_eating.append((opponent_piece.position, square.position))
                    elif piece.x > opponent_piece.x and piece.y > opponent_piece.y:
                        if opponent_piece_row_index - 1 == square_row_index and opponent_piece.y - 1 == square.y:
                            possible_eating.append((opponent_piece.position, square.position))
                    elif piece.x < opponent_piece.x and piece.y < opponent_piece.y:
                        if opponent_piece_row_index + 1 == square_row_index and opponent_piece.y + 1 == square.y:
                            possible_eating.append((opponent_piece.position, square.position))
                    elif piece.x < opponent_piece.x and piece.y > opponent_piece.y:
                        if opponent_piece_row_index + 1 == square_row_index and opponent_piece.y - 1 == square.y:
                            possible_eating.append((opponent_piece.position, square.position))
    if piece.queen == True:
        possible_moves = possible_moves_for_queen(piece)
        # for move in possible_moves:
    ###### OGARNĄĆ BICIE DLA KRÓLÓWKI 

    if len(possible_eating) == 0:
        return False
    else:
        return (piece.position, possible_eating)
                        
                        
def check_must_eat(player_pieces, opponent_pieces):
    pieces_can_eat = []              
    for piece in player_pieces:
        if possible_eating(piece, opponent_pieces) != False:
            pieces_can_eat.append(piece)
    if len(pieces_can_eat) == 0:
        return False
    else:
        return True

def choose_piece_to_eat(player_pieces, opponent_pieces):
    pieces_to_eat = []
    print("You have the must eat!")
    for piece in player_pieces:
        if possible_eating(piece, opponent_pieces) != False:
            pieces_to_eat.append(possible_eating(piece, opponent_pieces))
    for piece in pieces_to_eat:
        print(f"{piece[0][0]}{piece[0][1]}", end = " ")
    print("\r")
    while True:
        try:
            choose_piece = input("Choose a piece to eat: ").capitalize()
            for piece in pieces_to_eat:
                if (choose_piece[0], int(choose_piece[1])) == piece[0]:
                    return piece
        except ValueError:
            print("You must choose from the following pieces!")
            continue
        
def eating(piece_and_opponent_piece, player_pieces, opponent_pieces):
    player_piece_row = piece_and_opponent_piece[0][0]
    player_piece_column = int(piece_and_opponent_piece[0][1])
    board.display()
    if len(piece_and_opponent_piece[1]) == 1:
        opponent_piece_row = piece_and_opponent_piece[1][0][0][0]
        opponent_piece_column = int(piece_and_opponent_piece[1][0][0][1])
        for piece in player_pieces:
            if piece.position == (player_piece_row, player_piece_column):
                for square in white_squares:
                    if square.position == piece_and_opponent_piece[1][0][1]:
                        white_squares.remove(square)
                White(piece.position[0], piece.position[1])
                piece.position = piece_and_opponent_piece[1][0][1]
                change_position(piece, piece_and_opponent_piece[1][0][1][0], piece_and_opponent_piece[1][0][1][1])
                board.board[Square.rows_letters.index(piece.position[0])][piece.position[1] - 1] = piece
        for piece in opponent_pieces:
            if piece.position == (opponent_piece_row, opponent_piece_column):
                opponent_pieces.remove(piece)
                White(opponent_piece_row, opponent_piece_column)
    else:
        for piece in piece_and_opponent_piece[1]:
            print(f"{piece[0][0]}{piece[0][1]}", end = " ")
        print("\r")
        while True:
            try:
                choose_piece_to_be_eaten = input("Choose a piece to be eaten: ").capitalize()
                opponent_piece_row = choose_piece_to_be_eaten[0]
                opponent_piece_column = int(choose_piece_to_be_eaten[1])
            except ValueError:
                print("You must choose from the following pieces!")
                continue
            break
        for piece in player_pieces:
            if piece.position == (player_piece_row, player_piece_column):
                for pair in piece_and_opponent_piece[1]:
                    if (opponent_piece_row, opponent_piece_column) == pair[0]:
                        for square in white_squares:
                            if square.position == piece_and_opponent_piece[1][0][1]:
                                white_squares.remove(square)
                        White(piece.position[0], piece.position[1])
                        change_position(piece, pair[1][0], pair[1][1])
                        board.board[Square.rows_letters.index(piece.position[0])][piece.position[1] - 1] = piece
        for piece in opponent_pieces:
            if piece.position == (opponent_piece_row, opponent_piece_column):
                opponent_pieces.remove(piece)
                White(opponent_piece_row, opponent_piece_column)
    

        
def choose_piece_to_move(player_pieces):
    while True:
        try:
            selected_piece = input("Select a piece's row [\"A\"-\"H\"] and column [1-8]: ").capitalize()
            selected_piece_x = selected_piece[0]
            selected_piece_y = int(selected_piece[1])
            if all(piece.position != (selected_piece_x, selected_piece_y) for piece in player_pieces):
                raise ValueError   
        except ValueError:
            print("There is no such piece, try again.")
            continue
        break
    for piece in player_pieces:
        if piece.position == (selected_piece_x, selected_piece_y):
            piece.selected = True
            return piece

def move_for_user(piece):
    options = []
    piece_row = Square.rows_letters.index(piece.position[0])
    piece_column = piece.position[1]
    for square in white_squares:
        if square.position == (Square.rows_letters[piece_row - 1], piece_column + 1) or square.position == (Square.rows_letters[piece_row - 1], piece_column - 1):
            options.append(square.position)
    board.display()
    for option in options:
        print(f"{option[0]}{option[1]}", end= " ")
    print("\r")
    if len(options) == 0:
        return False
    while True:
        try:
            selected_place = input("Choose a square where you want to move the piece: ").capitalize()
            selected_place_x = selected_place[0]
            selected_place_y = int(selected_place[1])
            if (selected_place_x, selected_place_y) not in options:
                raise ValueError
        except ValueError:
            print("You must choose from the following options")
            continue
        break
    for square in white_squares:
        if square.position == (selected_place_x, selected_place_y):
            white_squares.remove(square)
    White(piece.position[0], piece.position[1])
    change_position(piece, selected_place_x, selected_place_y)
    board.board[Square.rows_letters.index(piece.position[0])][piece.position[1] - 1] = piece
    piece.selected = False
    return True
    
def move_for_computer(piece):
    options = []
    piece_row = Square.rows_letters.index(piece.position[0])
    piece_column = piece.position[1]
    for square in white_squares:
        if square.position == (Square.rows_letters[piece_row + 1], piece_column + 1) or square.position == (Square.rows_letters[piece_row + 1], piece_column - 1):
            options.append(square.position)
    board.display()
    for option in options:
        print(f"{option[0]}{option[1]}", end= " ")
    print("\r")
    if len(options) == 0:
        return False
    while True:
        try:
            selected_place = input("Choose a square where you want to move the piece: ").capitalize()
            selected_place_x = selected_place[0]
            selected_place_y = int(selected_place[1])
            if (selected_place_x, selected_place_y) not in options:
                raise ValueError
        except ValueError:
            print("You must choose from the following options")
            continue
        break
    for square in white_squares:
        if square.position == (selected_place_x, selected_place_y):
            white_squares.remove(square)
    White(piece.position[0], piece.position[1])
    change_position(piece, selected_place_x, selected_place_y)
    board.board[Square.rows_letters.index(piece.position[0])][piece.position[1] - 1] = piece
    piece.selected = False
    return True

def change_position(piece, x, y):
    if isinstance(piece, UserPiece) and x == "A":
        piece.queen = True
    if isinstance(piece, ComputerPiece) and x == "H":
        piece.queen = True
    piece.x = x
    piece.y = y
    piece.position = (x, y)
    
def possible_moves_for_queen(piece):
    upleft = []
    upright = []
    downleft = []
    downright = []
    index = Square.rows_letters.index(piece.x)
    y = piece.y
    while index > 0 and y > 1:
        index -= 1 
        y -= 1
        upleft.append((Square.rows_letters[index], y))
    index = Square.rows_letters.index(piece.x)
    y = piece.y
    while index > 0 and y < 8:
        index -= 1
        y += 1
        upright.append((Square.rows_letters[index], y))
    index = Square.rows_letters.index(piece.x)
    y = piece.y
    while index < 7 and y > 1:
        index += 1
        y -= 1
        downleft.append((Square.rows_letters[index], y))
    index = Square.rows_letters.index(piece.x)
    y = piece.y
    while index < 7 and y < 8:
        index += 1
        y += 1
        downright.append((Square.rows_letters[index], y))
    all_directions = [upleft, upright, downleft, downright]
    result_upleft = []
    result_upright = []
    result_downleft = []
    result_downright = []
    counter = 0
    while counter <= 3:
        for position in all_directions[counter]:
            for square in white_squares:
                if square.position == position:
                    if counter == 0:
                        result_upleft.append(position)
                    elif counter == 1:
                        result_upright.append(position)
                    elif counter == 2:
                        result_downleft.append(position)
                    elif counter == 3:
                        result_downright.append(position)
        counter += 1
        
    return result_upleft, result_upright, result_downleft, result_downright 