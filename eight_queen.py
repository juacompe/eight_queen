#-*- coding: utf-8 -*-
from validate_board import validate_board, get_diagonal_positions
from utils import to_coordinate_pair, all_positions, QUEEN, get_queen_index, is_queen

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
    queen_positions = [starting_at]
    safe_positions = find_safe_positions(queen_positions, all_positions)

    for i in range(1, 7):
        board, queen_position = safely_put_one_more_queen(board, safe_positions)
        queen_positions.append(queen_position)
        safe_positions = find_safe_positions(queen_positions, safe_positions)

    return board 

def safely_put_one_more_queen(board, positions=None):
    positions = positions or all_positions
    safe_positions_left = -1 
    best_position = None
    for position in positions:
        result_board = put_queen(board, position)
        board_is_still_valid = validate_board(result_board) 
        more_queen_was_added = count_queen(result_board) > count_queen(board)
        if board_is_still_valid and more_queen_was_added:
            queen_positions = find_queen_positions(result_board)
            safe_positions = find_safe_positions(queen_positions, positions)
            if len(safe_positions) > safe_positions_left:
                safe_positions_left = len(safe_positions) 
                best_position = position
                best_result = result_board
    if best_position == None:
        raise CannotPutMoreQueenException('Not expected here')
    print '%s' % best_position
    return best_result, best_position

def count_queen(board):
    return board.count(QUEEN) 
    
def find_queen_positions(board):
    queen_positions = [ position for position in all_positions if is_queen(board, position) ]
    return queen_positions 

def find_safe_positions(queen_positions, safe_positions):
    safe_positions = set(safe_positions)
    for queen_position in queen_positions:
        column, row = to_coordinate_pair(queen_position)
        all_positions_in_the_column = positions_in_the_same_column(column) 
        all_positions_in_the_row = positions_in_the_same_row(row) 
        all_diagonal_positions = get_diagonal_positions(queen_position)
        safe_positions = safe_positions - set(all_positions_in_the_column)
        safe_positions = safe_positions - set(all_positions_in_the_row)
        safe_positions = safe_positions - set(all_diagonal_positions)
    return safe_positions

def positions_in_the_same_column(column):
    return [ position for position in all_positions if position.count(column) ]

def positions_in_the_same_row(row):
    return [ position for position in all_positions if position.count(row) ]

