#-*- coding: utf-8 -*-
from validate_board import validate_board
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

def safely_put_one_more_queen(board):
    for position in all_positions:
        result_board = put_queen(board, position)
        board_is_still_valid = validate_board(result_board) 
        more_queen_was_added = count_queen(result_board) > count_queen(board)
        print '>> %s (valid: %s, added: %s)' % (position, board_is_still_valid, more_queen_was_added)
        if position == 'e5':
            print board
        if board_is_still_valid and more_queen_was_added:
            print '(%s)' % position
            return result_board
    raise CannotPutMoreQueenException('Not expected here')

def count_queen(board):
    return board.count(QUEEN) 
    
