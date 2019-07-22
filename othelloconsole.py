#Alvin Nguyen 28864658
#
#Project 4
#

import othellogamelogic


def run_user_interface():
    print("FULL")
    rows = othellogamelogic.board_rows()
    cols = othellogamelogic.board_cols()
    
    first_move = othellogamelogic.player_move()
    placement = othellogamelogic.player_placement()
    win_condition = othellogamelogic.winning_condition()

    board = othellogamelogic.make_board(rows, cols) #makes empty 2d list
    board = othellogamelogic.determine_start_position(board, placement, rows, cols) #sets
    #default position of pieces; updates the board
    othellogamelogic.piece_count(board) #prints count of B's and W's
    othellogamelogic.print_board(board, rows, cols) #prints the board
    current_move = othellogamelogic.current_player_move(first_move) #prints the current player's move
    print()
    print(current_move)
    move = othellogamelogic.ask_move(first_move) #asks for input of first player's move
    othellogamelogic.is_valid_move(move[0], move[1], rows, cols, board, first_move)
    othellogamelogic.print_board(board, rows, cols)
    current_move = othellogamelogic.switch_player(current_move)
    current_move = othellogamelogic.current_player_move(current_move)
    print()
    print(current_move)
    move = othellogamelogic.ask_move(current_move)
    print(move)
    othellogamelogic.is_valid_move(move[0], move[1], rows, cols, board, current_move)
    othellogamelogic.print_board(board, rows, cols)
    
if __name__ == '__main__':
    run_user_interface()
