#-*- coding: utf-8 -*-

def get_board(queen_positions):
    output = u"""
      a b c d e f g h
    8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
    7 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
    6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
    5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
    4 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
    3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
    2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
    1 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
    """
    for queen_position in queen_positions:
        output = put_queen(output, queen_position) 
    return output 

def put_queen(board, position):
    QUEEN = u'♛'
    column_indexes = {
        'a': 2,
        'b': 4,
        'c': 6,
        'd': 8,
        'e': 10,
        'f': 12,
        'g': 14,
        'h': 16,
    }
    column, row = to_coordinate_pair(position)
    index_at_beginning_of_row = board.find(row)
    column_index = column_indexes[column]
    queen_index = index_at_beginning_of_row + column_index
    board_list = list(board)
    board_list[queen_index] = QUEEN
    return "".join(board_list)

def to_coordinate_pair(position):
    return position[0], position[1]
