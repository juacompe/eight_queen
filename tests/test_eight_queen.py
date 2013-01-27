#-*- coding: utf-8 -*-
from eight_queen import get_board, put_queen, solve_puzzle, count_queen, safely_put_one_more_queen, CannotPutMoreQueenException
from utils import is_queen, OutOfBoardException
from validate_board import validate_board
from test_fixture import empty_board, board_with_queen_at_a1
from unittest import TestCase


class TestDisplay(TestCase):
    def test_get_empty_board(self):
        queen_positions = [] 
        result = get_board(queen_positions) 
        assertLikes(self, empty_board, result)

    def test_get_board_with_a_queen_at_a1(self):
        queen_positions = ['a1'] 
        result = get_board(queen_positions)
        assertLikes(self, board_with_queen_at_a1, result)

    def test_get_board_with_3_queens_at_a1_b3_and_c5(self):
        queen_positions = ['a1', 'b3', 'c5'] 
        result = get_board(queen_positions)
        expected = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ♛ ◻ ◼ ◻ ◼ ◻
        4 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ♛ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ♛ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        """
        assertLikes(self, expected, result)

        
class TestPutQueen(TestCase):
    def test_put_queen_at_a1(self):
        result = put_queen(empty_board, 'a1')
        assertLikes(self, board_with_queen_at_a1, result)

    def test_put_queen_out_of_the_bound_at_row_9(self):
        self.assertRaises(OutOfBoardException, put_queen, empty_board, 'a9')
        
    def test_put_queen_out_of_the_bound_at_column_i(self):
        self.assertRaises(OutOfBoardException, put_queen, empty_board, 'i1')
        

class TestSolvePuzzle(TestCase):
    def test_solve_puzzle_starting_at_bottom_left_corner(self):
        starting_point = 'a1'
        board = solve_puzzle(starting_point) 
        self.assertTrue(is_queen(board, 'a1'))
        self.assertTrue(validate_board(board))
        self.assertEquals(8, count_queen(board))

    def test_solve_puzzle_starting_at_bottom_right_corner(self):
        starting_point = 'h1'
        board = solve_puzzle(starting_point) 
        self.assertTrue(is_queen(board, 'h1'))
        self.assertTrue(validate_board(board))
        self.assertEquals(8, count_queen(board))

    def test_solve_puzzle_starting_at_top_right_corner(self):
        starting_point = 'h8'
        board = solve_puzzle(starting_point) 
        self.assertTrue(is_queen(board, 'h8'))
        self.assertTrue(validate_board(board))
        self.assertEquals(8, count_queen(board))

    def test_solve_puzzle_starting_at_top_left_corner(self):
        starting_point = 'a8'
        board = solve_puzzle(starting_point) 
        self.assertTrue(is_queen(board, 'a8'))
        self.assertTrue(validate_board(board))
        self.assertEquals(8, count_queen(board))

    def test_solve_puzzle_starting_at_middle_of_the_board(self):
        starting_point = 'd5'
        board = solve_puzzle(starting_point) 
        self.assertTrue(is_queen(board, 'd5'))
        self.assertTrue(validate_board(board))
        self.assertEquals(8, count_queen(board))


class TestSafelyPutOneMoreQueen(TestCase):
    """
    Safely put one more queen put a queen on a given board
    without let any queen kill each other
    """
    def test_safely_put_one_more_queen_on_empty_board(self):
        board = get_board([]) 
        board = safely_put_one_more_queen(board)
        self.assertEquals(1, count_queen(board))
        self.assertTrue(validate_board(board))

    def test_safely_put_one_more_queen_on_a_board_with_queen_at_a1(self):
        board = safely_put_one_more_queen(board_with_queen_at_a1)
        self.assertEquals(2, count_queen(board))
        self.assertTrue(validate_board(board))

    def test_safely_put_one_more_queen_on_a_board_with_queen_at_a1_and_b3(self):
        board_with_queen_at_a1_and_b3 = put_queen(board_with_queen_at_a1, 'b3')
        board = safely_put_one_more_queen(board_with_queen_at_a1_and_b3)
        self.assertEquals(3, count_queen(board))
        self.assertTrue(validate_board(board))

    def test_safely_put_one_more_queen_on_a_board_with_knight_pattern_starting_from_a1(self):
        board = get_board(['a1', 'b3', 'c5', 'd7'])
        column_e = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']
        board = safely_put_one_more_queen(board, column_e)
        self.assertEquals(5, count_queen(board))
        self.assertTrue(validate_board(board))
        self.assertTrue(is_queen(board, 'e2'))

    def test_safely_put_one_more_queen_on_a_board_with_knight_pattern_starting_from_h8(self):
        board = get_board(['h8', 'g6', 'f4', 'e2'])
        column_d = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8']
        board = safely_put_one_more_queen(board, column_d)
        self.assertEquals(5, count_queen(board))
        self.assertTrue(validate_board(board))
        self.assertTrue(is_queen(board, 'd7'))

    def test_cannot_safely_put_one_more_queen_on_a_full_board(self):
        """
        Full board is a board that already has 8 queens
        """
        eight_queens = ['a1', 'b3', 'c5', 'd7', 'e2', 'f4', 'g6', 'h8']
        full_board = get_board(eight_queens)
        self.assertRaises(CannotPutMoreQueenException, safely_put_one_more_queen, full_board)


class TestIsQueen(TestCase):
    def test_a1_is_queen(self):
        """
        test the right column, the right row
        """
        result = is_queen(board_with_queen_at_a1, 'a1') 
        self.assertTrue(result)

    def test_a8_is_not_queen(self):
        """
        test the right column, wrong row
        """
        result = is_queen(board_with_queen_at_a1, 'a8') 
        self.assertFalse(result)

    def test_h1_is_not_queen(self):
        """
        test the right row, wrong column 
        """
        result = is_queen(board_with_queen_at_a1, 'h1') 
        self.assertFalse(result)

class TestCountQueen(TestCase):
    def test_count_queen_on_empty_board(self):
        number_of_queens = count_queen(empty_board)
        self.assertEquals(0, number_of_queens)

    def test_count_queen_on_board_with_queen_at_a1(self):
        number_of_queens = count_queen(board_with_queen_at_a1)
        self.assertEquals(1, number_of_queens)



def assertLikes(test, expected, result):
    """
    Assert that 2 strings are equal if the whitespace is ignored
    """
    test.assertEquals(expected.replace(' ', ''), result.replace(' ', ''))
