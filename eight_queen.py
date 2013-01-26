#-*- coding: utf-8 -*-
from validate_board import validate_board, QUEEN

class OutOfBoardException(Exception): pass
class CannotPutMoreQueenException(Exception): pass

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
    if int(row) > 8:
        print 'Row %s is not expected' % row
        raise OutOfBoardException()

    if not column in column_indexes.keys():
        print 'Column %s is not expected' % column 
        raise OutOfBoardException()
        
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

def solve_puzzle(starting_at):
    board = get_board([starting_at])
    board = safely_put_one_more_queen(board)
    board = safely_put_one_more_queen(board)
    board = safely_put_one_more_queen(board)
    board = safely_put_one_more_queen(board)
    board = safely_put_one_more_queen(board)
    board = safely_put_one_more_queen(board)
    board = safely_put_one_more_queen(board)
    return board 

def safely_put_one_more_queen(board):
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
    for position in all_positions:
        result_board = put_queen(board, position)
        board_is_still_valid = validate_board(result_board) 
        more_queen_was_added = count_queen(result_board) > count_queen(board)
        if board_is_still_valid and more_queen_was_added:
            return result_board
    raise CannotPutMoreQueenException('Not expected here')

def is_queen(board, position):
    queen_index = get_queen_index(board, position)
    return board[queen_index] == QUEEN 

def count_queen(board):
    return board.count(QUEEN) 
    
