#Alvin Nguyen 28864658
#
#Project 4
#

def board_rows():
    while True:
        num_rows = int(input())
        if 4 <= num_rows <= 16 and num_rows % 2 == 0:
            return num_rows
        else:
            print("Row # must be 4-16 & even. Try again.")
            continue

def board_cols():
    while True:
        num_col = int(input())
        if 4 <= num_col <= 16 and num_col % 2 == 0:
            return num_col
        else:
            print("Column # must be 4-16 & even. Try again.")
            continue
        
def make_board(rows: int, cols: int):
    board = []
    for row in range(rows):
        sublist = []
        board.append(sublist)
        for col in range(cols):
            sublist.append(".")
    return board

def print_board(board, rows, cols):
    for row in range(rows):
        full_str = ""
        for col in range(cols):
            full_str += str(board[row][col])
        new_board = space_board(full_str)
        print(new_board)

def space_board(board: str):
    new_board = ""
    for char in board:
        new_board += char + "  "
    return new_board

def replace_char_black(current, rows, cols):
    current[rows][cols] = "B"


def replace_char_white(current, rows, cols):
    current[rows][cols] = "W"


def determine_start_position(current, placement, rows, cols):
    rows_index = int((rows/2)) - 1
    cols_index = int((cols/2)) - 1
    if placement == "B":
        replace_char_black(current, rows_index, cols_index)
        replace_char_black(current, rows_index + 1, cols_index + 1)
        replace_char_white(current, rows_index + 1, cols_index)
        replace_char_white(current, rows_index, cols_index + 1)
        return current
    else:
        replace_char_white(current, rows_index, cols_index)
        replace_char_white(current, rows_index + 1, cols_index + 1)
        replace_char_black(current, rows_index + 1, cols_index)
        replace_char_black(current, rows_index, cols_index + 1)
        return current
    
def piece_count(current):
    black_count = 0
    white_count = 0
    for sublist in current:
        for value in sublist:
            if value == "B":
                black_count += 1
            elif value == "W":
                white_count += 1
            else:
                continue
    print("B: " + str(black_count) + "  " + "W: " + str(white_count))

def current_player_move(player_move):
    if player_move == "B":
        print("TURN: B")
        return player_move
    else:
        print("TURN: W")
        return player_move
        
def switch_player(player_move):
    if player_move == "B":
        player_move = "W"
        return player_move
    elif player_move == "W":
        player_move = "B"
        return player_move
"""
def is_empty_space(row: str, col: str, current) -> bool:
    row = int(row) - 1
    col = int(col) - 1
    if current[row][col] == ".":
        return True
    else:
        return False
"""

def ask_move(move):
    move_list = []
    move = player_move()
    move_list.append(move)
    for item in move_list:
        move_list = item.split(" ")
        for index in range(len(move_list)):
            move_list[index] = int(move_list[index]) - 1
    return move_list
    
def player_move():

    player_move = input()
    return player_move

def player_placement():

    player_placement = input()
    return player_placement

def winning_condition():

    winning_condition = input()
    return winning_condition

def is_on_board(row: int, col: int, board_row, board_col) -> bool:
    return 0 <= row <= board_row - 1 and 0 <= col <= board_col - 1

def is_empty_space(row, col, board) -> bool:
    return board[row][col] == "."

def mark_tile(row, col, board) -> None:
    board[row][col] = "X"
    
def is_valid_move(row: int, col: int, board_row, board_col, board, current_player):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

    if not is_empty_space(row, col, board):
        return False
    
    if current_player == "B":
        opposite_player = "W"
    elif current_player == "W":
        opposite_player = "B"
        
    valid_move = True
    valid_direction = []
    for direction in directions:
        distance = 1
        new_row = row + (direction[0] * distance)
        new_col = col + (direction[1] * distance)
        valid = False
        while is_on_board(new_row, new_col, board_row, board_col):
            if board[new_row][new_col] == ".":
                print("Not valid direction")
                break
            elif board[new_row][new_col] == current_player:
                print("Not valid direction")
                break
            elif board[new_row][new_col] == opposite_player:
                valid = True
                valid_direction.append(direction)
                break
            distance += 1
            new_row = row + (direction[0] * distance)
            new_col = col + (direction[1] * distance)
        print(direction, new_row, new_col, valid, valid_direction)
        
    new_row = row
    new_col = col
    
    for direction in valid_direction:
        new_row = row + direction[0]
        new_col = col + direction[1]
        print(new_row, new_col)
        discs_to_flip = []
        if not is_on_board(new_row, new_col, board_row, board_col):
            print("End of direction")
            
        while board[new_row][new_col] == opposite_player:
            discs_to_flip.append([new_row, new_col])
            print("Keep going")
            new_row = new_row + direction[0]
            new_col = new_col + direction[1]
            if board[new_row][new_col] == current_player:
                print("Valid move confirmed")
                board[row][col] = current_player
                break
            elif is_empty_space(new_row, new_col, board) or not is_on_board(new_row, new_col, board_row, board_col):
                print("Not valid direction")
                break
        print(discs_to_flip)
            



