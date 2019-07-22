BLACK = "B"
WHITE = "W"
EMPTY = ""

directions = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

class GameState:

    def __init__(self, win, row, column, placement, turn):

        self.board_row = row
        self.board_col = column

        self.player_turn = turn

        self.first_placement = placement

        self.win_condition = win

        self.board = []
        for row in range(row):
            sublist = []
            self.board.append(sublist)
            for col in range(column):
                sublist.append(".")
        return self.board
    """
    def replace_char_black(self, board):
        board[
            
    def determine_start_position(self, player, opposite_player):
    """
    def alternate_turns(self):
        if self.player_turn == BLACK:
            self.player_turn = WHITE
        else:
            self.player_turn = BLACK
        return self.player_turn
    
    def determine_player_turn(self):
        self.opposite_player = BLACK
        
        if self.player_turn == BLACK:
            self.opposite_player = WHITE
        else:
            self.opposite_player = BLACK
            
    def is_on_board(self, row, col) -> bool:
        return 0 <= row < self.board_row and 0 <= col < self.board_col

    def is_valid_move(self) -> None:
        
        for direction in directions:
            distance = 0
            new_row = self.board_row
            new_col = self.board_col
            while is_on_board(new_row, new_col):
    
        
        
