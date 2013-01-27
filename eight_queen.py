#-*- coding: utf-8 -*-
from validate_board import validate_board, get_diagonal_positions
from utils import to_coordinate_pair, all_positions, QUEEN, get_queen_index

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

def put_queen(board, position):
    queen_index = get_queen_index(board, position)
    board_list = list(board)
    board_list[queen_index] = QUEEN
    return "".join(board_list)

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

def safely_put_one_more_queen(board, positions=None):
    positions = positions or all_positions
    min_used = 64
    best_position = None
    for position in positions:
        result_board = put_queen(board, position)
        board_is_still_valid = validate_board(result_board) 
        more_queen_was_added = count_queen(result_board) > count_queen(board)
        if board_is_still_valid and more_queen_was_added:
            diagonal_positions = get_diagonal_positions(position)
            used = len(diagonal_positions)
            if used < min_used:
                min_used = used
                best_position = position
                best_result = result_board
    if best_position == None:
        raise CannotPutMoreQueenException('Not expected here')
    print '%s (%s)' % (best_position, min_used)
    return best_result

def count_queen(board):
    return board.count(QUEEN) 
    
