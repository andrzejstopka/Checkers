from packages.board_package.board import *

# def computer_must_eat():
#     try:
#         result = {}
#         for computer_piece in computer_pieces:
#             next_row = Square.rows_letters[Square.rows_letters.index(computer_piece.x) + 2]
#             row = Square.rows_letters[Square.rows_letters.index(computer_piece.x) + 1]
#             first_y = computer_piece.y - 1
#             second_y = computer_piece.y + 1
#             for user_piece in user_pieces:
#                 index = Square.rows_letters.index(next_row)
#                 if computer_piece.queen == True:
#                     if user_piece.position in computer_piece.move():
#                         index = Square.rows_letters.index(user_piece.position[0])
#                         if index > 0 and index < 7:
#                                 if computer_piece in result and ((isinstance(board.board[index - 1][user_piece.y], White) and (isinstance(board.board[index + 1][user_piece.y - 2], White) or board.board[index + 1][user_piece.y - 2] is computer_piece)) or (isinstance(board.board[index - 1][user_piece.y - 2], White) and (isinstance(board.board[index + 1][user_piece.y], White) or board.board[index + 1][user_piece.y] is computer_piece)) or (isinstance(board.board[index - 1][user_piece.y], White) and (isinstance(board.board[index + 1][user_piece.y - 2], White) or board.board[index - 1][user_piece.y - 2] is computer_piece)) or (isinstance(board.board[index - 1][user_piece.y - 2], White) and (isinstance(board.board[index + 1][user_piece.y], White) or board.board[index - 1][user_piece.y] is computer_piece))):
#                                     result[computer_piece] = result[computer_piece], user_piece
#                                 elif isinstance(board.board[index - 1][user_piece.y], White) and (isinstance(board.board[index + 1][user_piece.y - 2], White) or board.board[index + 1][user_piece.y - 2] is computer_piece):
#                                     result[computer_piece] = user_piece
#                                 elif isinstance(board.board[index - 1][user_piece.y - 2], White) and (isinstance(board.board[index + 1][user_piece.y], White) or board.board[index + 1][user_piece.y] is computer_piece):
#                                     result[computer_piece] = user_piece    
#                                 elif isinstance(board.board[index - 1][user_piece.y], White) and (isinstance(board.board[index + 1][user_piece.y - 2], White) or board.board[index - 1][user_piece.y - 2] is computer_piece):
#                                     result[computer_piece] = user_piece   
#                                 elif isinstance(board.board[index - 1][user_piece.y - 2], White) and (isinstance(board.board[index + 1][user_piece.y], White) or board.board[index - 1][user_piece.y] is computer_piece):
#                                     result[computer_piece] = user_piece           
        
#                 if computer_piece.queen == False:
#                         if computer_piece in result and ((user_piece.position == (row, first_y) and isinstance(board.board[index][first_y - 2], White) or user_piece.position == (row, second_y) and isinstance(board.board[index][first_y + 2], White))) :
#                             result[computer_piece] = result[computer_piece], user_piece
#                         elif user_piece.position == (row, first_y) and isinstance(board.board[index][first_y - 2], White):
#                             result[computer_piece] = user_piece
#                         elif user_piece.position == (row, second_y) and isinstance(board.board[index][first_y + 2], White):
#                             result[computer_piece] = user_piece   
                            
#         if len(result) == 0:
#             return False
#         print("You have the must eat! Choose a piece: ")
#         for key in result.keys():
#             print(f"{key.x}{key.y}", sep=" ", end=" ")
#         print("\r")
#         select_piece = input("Select a piece: ").capitalize()
#         for piece, square in result.items():
#             next_row = Square.rows_letters[Square.rows_letters.index(piece.x) + 2]
#             if select_piece == f"{piece.x}{str(piece.y)}":
#                 if isinstance(square, Piece):
#                     piece.selected = True
#                     board.display()
#                     if piece.queen == True:
#                         up_row = Square.rows_letters[Square.rows_letters.index(square.position[0]) + 1]
#                         down_row = Square.rows_letters[Square.rows_letters.index(square.position[0]) - 1]
#                         if piece.y > square.position[1] and piece.x > square.position[0]:
#                             piece.change_position(up_row, square.position[1] - 1)
#                         elif piece.y < square.position[1] and piece.x > square.position[0]:
#                             piece.change_position(up_row, square.position[1] + 1)
#                         elif piece.y > square.position[1] and piece.x < square.position[0]:
#                             piece.change_position(down_row, square.position[1] - 1)
#                         else:
#                             piece.change_position(down_row, square.position[1] + 1)
#                     elif piece.y > square.position[1]:
#                         piece.change_position(next_row, square.position[1] - 1)
#                     else:
#                         piece.change_position(next_row, square.position[1] + 1)
#                     piece.selected = False
#                     White(square.position[0], square.position[1])
#                     user_pieces.remove(square)
#                 elif isinstance(square, tuple):
#                     for option in square:
#                         print(f"{option.x}{option.y}", sep=" ", end=" ")
#                     print("\r")
#                     select_piece_to_eat = input("Choose a piece to eat: ").capitalize()
#                     for option in square:
#                         if select_piece_to_eat == f"{option.x}{str(option.y)}":
#                             piece.selected = True
#                             board.display()
#                             if piece.queen == True:
#                                 up_row = Square.rows_letters[Square.rows_letters.index(option.x) + 1]
#                                 down_row = Square.rows_letters[Square.rows_letters.index(option.x) - 1]
#                                 if piece.y > option.y and piece.x > option.x:
#                                     piece.change_position(up_row, option.y - 1)
#                                 elif piece.y < option.y and piece.x > option.x:
#                                     piece.change_position(up_row, option.y + 1)
#                                 elif piece.y > option.y and piece.x < option.x:
#                                     piece.change_position(down_row, option.y - 1)
#                                 else:
#                                     piece.change_position(down_row, option.y + 1)
#                             elif piece.y > option.y:
#                                 piece.change_position(next_row, option.y - 1)
#                             else:
#                                 piece.change_position(next_row, option.y + 1)
#                             piece.selected = False
#                             White(option.x, option.y)
#                             user_pieces.remove(option)    
#         return True    
#     except:
#         pass
# def computer_turn():
#     while True:
#         try:
#             select_piece = input("Computer Select a piece's row [\"A\"-\"H\"] and row [1-8]: ")
#             select_piece_x = select_piece[0].capitalize()
#             select_piece_y = int(select_piece[1])
#             if all(piece.position != (select_piece_x, select_piece_y) for piece in computer_pieces):
#                 raise ValueError                  
#         except ValueError:
#             print("There is no such piece, try again.")
#             continue
#         break
#     for piece in computer_pieces:
#         if piece.queen == False:
#             if piece.position == (select_piece_x, select_piece_y):
#                 piece.selected = True
#                 board.display()
#                 if piece.move() == False:
#                     print("The piece can't be moved")
#                     piece.selected = False
#                     return False
#                 piece.selected = False
#         else:
#             for square in piece.move():
#                 print(f"{square[0]}{square[1]}", sep=" ", end=" ")
#             print("\r")
#             while True:
#                 try:
#                     go = input("Choose where you want to move the piece: ")
#                     go = (go[0].upper(), int(go[1]))
#                     if go in piece.move():
#                         piece.change_position(go[0], go[1])
#                         break
#                 except ValueError:
#                     print("Enter a valid move, please try again.")
#                     continue