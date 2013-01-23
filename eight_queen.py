#-*- coding: utf-8 -*-

QUEEN = u'♛'

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

def get_queen_index(board, position):
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
    return index_at_beginning_of_row + column_index
 
def put_queen(board, position):
    queen_index = get_queen_index(board, position)
    board_list = list(board)
    board_list[queen_index] = QUEEN
    return "".join(board_list)

def to_coordinate_pair(position):
    return position[0], position[1]

def validate_board(board):
    rows_valid = True
    for row in range(1,9):
        row_valid = validate_row(str(row), board) 
        rows_valid = rows_valid and row_valid
    columns_valid = True
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for column in columns:
        column_valid = validate_column(column, board)
        columns_valid = columns_valid and column_valid
    return rows_valid and columns_valid

def validate_row(row, board):
    row_index = board.find(row)
    row_starts = row_index + 1
    row_ends = board.find('\n', row_starts)
    row_to_validate = board[row_starts: row_ends]
    return row_to_validate.count(QUEEN) <= 1 

def validate_column(column, board):
    column_to_validate = get_column(column, board) 
    return column_to_validate.count(QUEEN) <= 1

def get_column(column, board):
    board = board.replace(' ', '')
    indexes_of_the_column = get_column_indexes(column, board)
    column_to_validate = ''.join([ board[index] for index in indexes_of_the_column ])
    return column_to_validate 

def get_column_indexes(column, board):
    """
    return list of xy while:
    - x depends on row and
    - y depends on column
    """
    board = board.replace(' ', '')
    all_y = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8,
    }
    y = all_y[column]
    all_x = range(1, 9) 
    return [ int(str(x) + str(y)) for x in all_x ]

def solve(starting_at):
    return get_board([starting_at])

def is_queen(board, position):
    queen_index = get_queen_index(board, position)
    return board[queen_index] == QUEEN 

    
