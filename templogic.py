"""
    not_adjacent = True
    for direction in directions_dpad:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if _is_on_board(new_row, new_col, board_row, board_col):
            if board[new_row][new_col] == current_player:
                not_adjacent = False
                break
    if not not_adjacent:
        return [False]
    """
    valid_move = True
    valid_directions_temp = []
    for direction in directions:
        distance = 1
        new_row = row + (direction[0] * distance)
        new_col = col + (direction[1] * distance)
        valid = False
        while _is_on_board(new_row, new_col, board_row, board_col):
            if _is_empty_space(new_row, new_col, board):
                break
            #elif board[new_row][new_col] == opposite_player:
            elif board[new_row][new_col] == current_player:
                valid = True
                valid_directions_temp.append(direction)
                break
            distance += 1
            new_row = row + (direction[0] * distance)
            new_col = col + (direction[1] * distance)
        print(direction, new_row, new_col, valid)
        
        valid_move = valid_move or valid
    valid_directions = []
    for direction in valid_directions_temp:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if board[new_row][new_col] == opposite_player:
            valid_directions.append(direction)
    valid_move = len(valid_directions) >= 1
    return [valid_move, valid_directions]
