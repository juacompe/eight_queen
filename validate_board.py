#-*- coding: utf-8 -*-
QUEEN = u'♛'

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


