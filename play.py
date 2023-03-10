from packages.board import *
import random
from time import sleep

def possible_eating(piece, opponent_pieces, player_pieces):
    possible_eating = []
    piece_row_index = Square.rows_letters.index(piece.x)
    if piece.queen == True:
        possible_eating = []
        possible_moves = possible_moves_for_queen(piece)
        try:
            for move_list in possible_moves:
                for move in move_list:
                    for opponent_piece in opponent_pieces:
                        for square in white_squares:
                            move_index_x = Square.rows_letters.index(move[0])
                            move_y = move[1]
                            if possible_moves.index(move_list) == 0:
                                if opponent_piece.position == (Square.rows_letters[move_index_x - 1], move_y - 1):
                                    if square.position == (Square.rows_letters[move_index_x - 2], move_y - 2):
                                        possible_eating.append((opponent_piece, square))
                            if possible_moves.index(move_list) == 1:
                                if opponent_piece.position == (Square.rows_letters[move_index_x - 1], move_y + 1):
                                    if square.position == (Square.rows_letters[move_index_x - 2], move_y + 2):
                                        possible_eating.append((opponent_piece, square))
                            if possible_moves.index(move_list) == 2:
                                if opponent_piece.position == (Square.rows_letters[move_index_x + 1], move_y - 1):
                                    if square.position == (Square.rows_letters[move_index_x + 2], move_y - 2):
                                        possible_eating.append((opponent_piece, square))
                            if possible_moves.index(move_list) == 3:
                                if opponent_piece.position == (Square.rows_letters[move_index_x + 1], move_y + 1):
                                    if square.position == (Square.rows_letters[move_index_x + 2], move_y + 2):
                                        possible_eating.append((opponent_piece, square))     
        except IndexError:
            pass 
    for opponent_piece in opponent_pieces:
        opponent_piece_row_index = Square.rows_letters.index(
            opponent_piece.x)
        rows_difference1 = piece_row_index + 1 == opponent_piece_row_index or piece_row_index - 1 == opponent_piece_row_index
        column_difference1 = piece.y - 1 == opponent_piece.y or piece.y + 1 == opponent_piece.y
        if rows_difference1 == True and column_difference1 == True:
            for square in white_squares:
                square_row_index = Square.rows_letters.index(square.x)
                if piece.x > opponent_piece.x and piece.y < opponent_piece.y:
                    if opponent_piece_row_index - 1 == square_row_index and opponent_piece.y + 1 == square.y:
                        possible_eating.append((opponent_piece, square))
                elif piece.x > opponent_piece.x and piece.y > opponent_piece.y:
                    if opponent_piece_row_index - 1 == square_row_index and opponent_piece.y - 1 == square.y:
                        possible_eating.append((opponent_piece, square))
                elif piece.x < opponent_piece.x and piece.y < opponent_piece.y:
                    if opponent_piece_row_index + 1 == square_row_index and opponent_piece.y + 1 == square.y:
                        possible_eating.append((opponent_piece, square))
                elif piece.x < opponent_piece.x and piece.y > opponent_piece.y:
                    if opponent_piece_row_index + 1 == square_row_index and opponent_piece.y - 1 == square.y:
                        possible_eating.append((opponent_piece, square))
    if len(possible_eating) == 0:
        return False
    else:
        return (piece, possible_eating)


def check_must_eat(player_pieces, opponent_pieces):
    pieces_can_eat = []
    for piece in player_pieces:
        if possible_eating(piece, opponent_pieces, player_pieces) != False:
            pieces_can_eat.append(piece)
    if len(pieces_can_eat) == 0:
        return False
    else:
        return True


def choose_piece_to_eat(player_pieces, opponent_pieces):
    pieces_to_eat = []
    for piece in player_pieces:
        if possible_eating(piece, opponent_pieces, player_pieces) != False:
            pieces_to_eat.append(possible_eating(
                piece, opponent_pieces, player_pieces))
    if player_pieces == user_pieces:
        print("You have the must eat!")
        for piece in pieces_to_eat:
            print(f"{piece[0].position[0]}{piece[0].position[1]}", end=" ")
        print("\r")
        while True:
            try:
                choose_piece = input("Choose a piece to eat: ").capitalize()
                for piece in pieces_to_eat:
                    if (choose_piece[0], int(choose_piece[1])) == piece[0].position:
                        return piece
            except ValueError:
                print("You must choose from the following pieces!")
                continue
    else:
        return random.choice(pieces_to_eat)
        

def eating(piece_and_opponent_piece, player_pieces, opponent_pieces):
    player_piece_row = piece_and_opponent_piece[0].position[0]
    player_piece_column = int(piece_and_opponent_piece[0].position[1])
    if len(piece_and_opponent_piece[1]) == 1:
        opponent_piece_row = piece_and_opponent_piece[1][0][0].position[0]
        opponent_piece_column = int(
            piece_and_opponent_piece[1][0][0].position[1])
        for piece in player_pieces:
            if piece.position == (player_piece_row, player_piece_column):
                for square in white_squares:
                    if square.position == piece_and_opponent_piece[1][0][1].position:
                        white_squares.remove(square)
                White(player_piece_row, player_piece_column)
                change_position(
                    piece, piece_and_opponent_piece[1][0][1].position[0], piece_and_opponent_piece[1][0][1].position[1])
                board.board[Square.rows_letters.index(
                    piece.position[0])][piece.position[1] - 1] = piece
        for piece in opponent_pieces:
            if piece.position == (opponent_piece_row, opponent_piece_column):
                opponent_pieces.remove(piece)
                White(opponent_piece_row, opponent_piece_column)
    else:
        if player_pieces == user_pieces:
            for piece in piece_and_opponent_piece[1]:
                print(f"{piece[0].position[0]}{piece[0].position[1]}", end=" ")
            print("\r")
            while True:
                try:
                    choose_piece_to_be_eaten = input("Choose a piece to be eaten: ").capitalize()
                    opponent_piece_row = choose_piece_to_be_eaten[0]
                    opponent_piece_column = int(choose_piece_to_be_eaten[1])
                    if all(piece[0].position != (opponent_piece_row, opponent_piece_column) for piece in piece_and_opponent_piece[1]):
                        raise ValueError
                except ValueError:
                    print("You must choose from the following pieces!")
                    continue
                break
        else:
            choose_piece_to_be_eaten = random.choice(piece_and_opponent_piece[1])
            opponent_piece_row = choose_piece_to_be_eaten[0]
            opponent_piece_column = choose_piece_to_be_eaten[1]
        for piece in player_pieces:
            if piece.position == (player_piece_row, player_piece_column):
                for pair in piece_and_opponent_piece[1]:
                    if (opponent_piece_row, opponent_piece_column) == pair[0].position:
                        for square in white_squares:
                            if square.position == piece_and_opponent_piece[1][0][1].position:
                                white_squares.remove(square)
                        White(piece.position[0], piece.position[1])
                        change_position(
                            piece, pair[1].position[0], pair[1].position[1])
                        board.board[Square.rows_letters.index(
                            piece.position[0])][piece.position[1] - 1] = piece
        for piece in opponent_pieces:
            if piece.position == (opponent_piece_row, opponent_piece_column):
                opponent_pieces.remove(piece)
                White(opponent_piece_row, opponent_piece_column)


def choose_piece_to_move(player_pieces):
    if player_pieces == user_pieces:
        while True:
            try:
                selected_piece = input(
                    "Select a piece's row [\"A\"-\"H\"] and column [1-8]: ").capitalize()
                selected_piece_x = selected_piece[0]
                selected_piece_y = int(selected_piece[1])
                if all(piece.position != (selected_piece_x, selected_piece_y) for piece in player_pieces):
                    raise ValueError
            except ValueError:
                print("There is no such piece, try again.")
                continue
            break
    else:
        selected_piece = random.choice(player_pieces)
        selected_piece_x = selected_piece.position[0]
        selected_piece_y = selected_piece.position[1]
    for piece in player_pieces:
        if piece.position == (selected_piece_x, selected_piece_y):
            piece.selected = True
            return piece


def move(piece):
    if piece.queen == False:
        options = []
        piece_row = Square.rows_letters.index(piece.position[0])
        piece_column = piece.position[1]
        for square in white_squares:
            if isinstance(piece, UserPiece):
                if square.position == (Square.rows_letters[piece_row - 1], piece_column + 1) or square.position == (Square.rows_letters[piece_row - 1], piece_column - 1):
                    options.append(square.position)
            elif isinstance(piece, ComputerPiece):
                if square.position == (Square.rows_letters[piece_row + 1], piece_column + 1) or square.position == (Square.rows_letters[piece_row + 1], piece_column - 1):
                    options.append(square.position)
        board.display()
        if len(options) == 0:
            piece.selected = False
            return False
        if isinstance(piece, UserPiece):
            for option in options:
                print(f"{option[0]}{option[1]}", end=" ")
            print("\r")
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
        else:
            selected_place = random.choice(options)
            selected_place_x = selected_place[0]
            selected_place_y = selected_place[1]
        for square in white_squares:
            if square.position == (selected_place_x, selected_place_y):
                white_squares.remove(square)
        White(piece.position[0], piece.position[1])
        change_position(piece, selected_place_x, selected_place_y)
        board.board[Square.rows_letters.index(
            piece.position[0])][piece.position[1] - 1] = piece
        piece.selected = False
        return True
    elif piece.queen == True:
        list_possible_moves = possible_moves_for_queen(piece)
        if isinstance(piece, UserPiece):
            while True:
                try:
                    selected_place = input("Choose a place to go: ").capitalize()
                    selected_place_x = selected_place[0]
                    selected_place_y = int(selected_place[1])
                    if all(place != (selected_place_x, selected_place_y) for move_list in list_possible_moves for place in move_list):
                        raise ValueError
                except ValueError:
                    print("You must choose one from the following moves.")
                    continue
                break
        else:
            while True:
                selected_direction = random.choice(list_possible_moves)
                if len(selected_direction) > 0:
                    break
            selected_place = random.choice(selected_direction)
            selected_place_x = selected_place[0]
            selected_place_y = int(selected_place[1])
            
        for square in white_squares:
            if square.position == (selected_place_x, selected_place_y):
                white_squares.remove(square)
        White(piece.position[0], piece.position[1])
        change_position(piece, selected_place_x, selected_place_y)
        board.board[Square.rows_letters.index(piece.position[0])][piece.position[1] - 1] = piece
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
    if isinstance(piece, UserPiece):
        own_pieces = user_pieces
    else:
        own_pieces = computer_pieces
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
    try:
        upleft_max = max(piece.position[0] for piece in [piece for piece in own_pieces if piece.position in upleft])
        upright_max = max(piece.position[0] for piece in [piece for piece in own_pieces if piece.position in upright])
        downleft_min = min(piece.position[0] for piece in [piece for piece in own_pieces if piece.position in downleft])
        downright_min = min(piece.position[0] for piece in [piece for piece in own_pieces if piece.position in downright])
    except ValueError:
        pass
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
                        try:
                            if position[0] > upleft_max:
                                result_upleft.append(position)
                        except UnboundLocalError:
                            result_upleft.append(position)
                    elif counter == 1:
                        try:
                            if position[0] > upright_max:
                                result_upright.append(position)
                        except UnboundLocalError:
                            result_upright.append(position)
                    elif counter == 2:
                        try:
                            if position[0] < downleft_min:
                                result_downleft.append(position)
                        except UnboundLocalError:
                            result_downleft.append(position)
                    elif counter == 3:
                        try:
                            if position[0] < downright_min:
                                result_downright.append(position)
                        except UnboundLocalError:
                            result_downright.append(position)
        counter += 1
    return result_upleft, result_upright, result_downleft, result_downright

    