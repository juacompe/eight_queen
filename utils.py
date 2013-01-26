#-*- coding: utf-8 -*-

class OutOfBoardException(Exception): pass

QUEEN = u'♛'

all_positions = [
    'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
    'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
    'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
    'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
    'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
    'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
]
def to_coordinate_pair(position):
    return position[0], position[1]

def is_queen(board, position):
    queen_index = get_queen_index(board, position)
    return board[queen_index] == QUEEN 

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
    if int(row) > 8:
        print 'Row %s is not expected' % row
        raise OutOfBoardException()

    if not column in column_indexes.keys():
        print 'Column %s is not expected' % column 
        raise OutOfBoardException()
        
    index_at_beginning_of_row = board.find(row)
    column_index = column_indexes[column]
    return index_at_beginning_of_row + column_index
 
