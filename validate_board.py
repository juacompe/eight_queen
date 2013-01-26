#-*- coding: utf-8 -*-
from utils import to_coordinate_pair, all_positions, QUEEN, is_queen

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
    queen_positions = [ position for position in all_positions if is_queen(board, position) ]
    diagonally_valid = True
    for queen_position in queen_positions:
        diagonally_valid = diagonally_valid and validate_diagonally(queen_position, board)
    return rows_valid and columns_valid and diagonally_valid

def validate_row(row, board):
    row_index = board.find(row)
    row_starts = row_index + 1
    row_ends = board.find('\n', row_starts)
    row_to_validate = board[row_starts: row_ends]
    return row_to_validate.count(QUEEN) <= 1 

def validate_column(column, board):
    column_to_validate = get_column(column, board) 
    return column_to_validate.count(QUEEN) <= 1

def validate_diagonally(position, board):
    positions = get_diagonal_positions(position) 
    positions.append(position)
    queen_positions = [ position for position in positions if is_queen(board, position) ]
    return len(queen_positions) <= 1

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

def get_diagonal_positions(position):
    p1 = position
    diagonal_positions = [ p2 for p2 in all_positions if is_align_diagonally(p1, p2) ]
    return diagonal_positions 
    
def is_align_diagonally(position1, position2):
    column1, row1 = to_coordinate_pair(position1)
    column2, row2 = to_coordinate_pair(position2)
    all_y = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8,
    }
    x1 = int(row1)
    y1 = all_y[column1]
    x2 = int(row2)
    y2 = all_y[column2]
    same_position = (x1 == x2) and (y1 == y2)
    aligned_diagonally = (x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2)
    return (not same_position) and aligned_diagonally 

