from packages.new_board2 import *



def user_turn():
    select_piece_x = input("Select pieces's row [\"A\"-\"H\"]: ") 
    select_piece_y= int(input("Select pieces's column [1-8]: "))
    for piece in user_pieces:
        if piece.position == (select_piece_x, select_piece_y):
            piece.selected = True
            board.display()
            piece.move()
            piece.selected = False
            
        
        
while True:                
    board.display()
    user_turn()
            