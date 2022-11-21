from packages.board import *
from play import *


while True:
    while True:
        if len(computer_pieces) == 0:
            print("You win! Congratulations!")
            break
        board.display()
        if check_must_eat(user_pieces, computer_pieces):
            eating(choose_piece_to_eat(user_pieces, computer_pieces),
                   user_pieces, computer_pieces)
            continue
        if move(choose_piece_to_move(user_pieces)) == False:
            print("This piece can't be moved. Try again")
            continue
        break
    while True:
        if len(user_pieces) == 0:
            print("You lose.")
            break
        board.display()
        if check_must_eat(computer_pieces, user_pieces):
            eating(choose_piece_to_eat(computer_pieces, user_pieces),
                   computer_pieces, user_pieces)
            continue
        if move(choose_piece_to_move(computer_pieces)) == False:
            print("This piece can't be moved. Try again")
            continue
        break
