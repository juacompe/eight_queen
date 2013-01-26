#-*- coding: utf-8 -*-
from validate_board import validate_board, get_column, get_column_indexes, get_diagonal_positions, is_align_diagonally
from test_fixture import empty_board
from unittest import TestCase

class TestValidateBoard(TestCase):
    def test_empty_board_should_valid(self):
        valid = validate_board(empty_board)
        self.assertTrue(valid)

    def test_board_with_queens_at_a2_b4_c1_d3_e5_should_valid(self):
        board = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ♛ ◻ ◼ ◻
        4 ◻ ♛ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ♛ ◼ ◻ ◼ ◻
        2 ♛ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ◼ ◻ ♛ ◻ ◼ ◻ ◼ ◻
        """
        valid = validate_board(board)
        self.assertTrue(valid)

    def test_board_with_2_queens_in_row_1_should_not_valid(self):
        board = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        4 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ♛ ◻ ◼ ◻ ◼ ◻ ♛ ◻
        """
        valid = validate_board(board)
        self.assertFalse(valid)

    def test_board_with_2_queens_in_row_7_should_not_valid(self):
        board = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ◼ ◻ ◼ ♛ ♛ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        4 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        """
        valid = validate_board(board)
        self.assertFalse(valid)

    def test_board_with_2_queens_in_column_a_should_not_valid(self):
        board = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ♛ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        4 ♛ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        """
        valid = validate_board(board)
        self.assertFalse(valid)

    def test_board_with_2_queens_at_a1_and_h8_should_not_valid(self):
        board = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ♛
        7 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        4 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ♛ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        """
        valid = validate_board(board)
        self.assertFalse(valid)


class TestGetColumn(TestCase):
    def test_get_column_a(self):
        board = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ♛ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        4 ♛ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        """
        column = get_column('a', board)
        expected = u'◻♛◻◼♛◼◻◼'
        self.assertEqual(expected, column)
         

class TestGetColumnIndexes(TestCase):
    def test_get_column_indexes_of_a(self):
        board = u"""
         abcdefgh
        8◻◼◻◼◻◼◻◼
        7♛◻◼◻◼◻◼◻
        6◻◼◻◼◻◼◻◼
        5◼◻◼◻◼◻◼◻
        4♛◼◻◼◻◼◻◼
        3◼◻◼◻◼◻◼◻
        2◻◼◻◼◻◼◻◼
        1◼◻◼◻◼◻◼◻
        """
        result = get_column_indexes('a', board)
        expected_indexes = [11, 21, 31, 41, 51, 61, 71, 81]
        self.assertEquals(expected_indexes, result)
 
    def test_get_column_indexes_of_b(self):
        board = u"""
         abcdefgh
        8◻◼◻◼◻◼◻◼
        7♛◻◼◻◼◻◼◻
        6◻◼◻◼◻◼◻◼
        5◼◻◼◻◼◻◼◻
        4♛◼◻◼◻◼◻◼
        3◼◻◼◻◼◻◼◻
        2◻◼◻◼◻◼◻◼
        1◼◻◼◻◼◻◼◻
        """
        result = get_column_indexes('b', board)
        expected_indexes = [12, 22, 32, 42, 52, 62, 72, 82]
        self.assertEquals(expected_indexes, result)

    def test_get_column_indexes_of_h(self):
        board = u"""
         abcdefgh
        8◻◼◻◼◻◼◻◼
        7♛◻◼◻◼◻◼◻
        6◻◼◻◼◻◼◻◼
        5◼◻◼◻◼◻◼◻
        4♛◼◻◼◻◼◻◼
        3◼◻◼◻◼◻◼◻
        2◻◼◻◼◻◼◻◼
        1◼◻◼◻◼◻◼◻
        """
        result = get_column_indexes('h', board)
        expected_indexes = [18, 28, 38, 48, 58, 68, 78, 88]
        self.assertEquals(expected_indexes, result)
 
class TestGetDiagonalPositions(TestCase):
    def test_diagonal_positions_from_the_corner(self):
        result = get_diagonal_positions('a1')
        expected_indexes = ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8']
        self.assertEquals(set(expected_indexes), set(result))

    def test_diagonal_positions_from_the_middle_of_the_board(self):
        result = get_diagonal_positions('d5')
        expected_indexes = [
            'c6', 'b7', 'a8',      # to top left
            'c4', 'b3', 'a2',      # to bottom left 
            'e6', 'f7', 'g8',      # to top right
            'e4', 'f3', 'g2', 'h1' # to bottom right
        ]
        self.assertEquals(set(expected_indexes), set(result))

class TestIsAlignedDiagonally(TestCase):
    def test_is_align_diagonally_towards_bottom_left(self):
        position1 = 'g8'
        position2_list = ['f7', 'e6', 'd5', 'c4', 'b3', 'a2']
        for position2 in position2_list:
            result = is_align_diagonally(position1, position2)
            self.assertTrue(result, position2)

    def test_is_align_diagonally_towards_top_left(self):
        position1 = 'h2'
        position2_list = ['g3', 'f4', 'e5', 'd6', 'c7', 'b8']
        for position2 in position2_list:
            result = is_align_diagonally(position1, position2)
            self.assertTrue(result, position2)

    def test_is_align_diagonally_towards_bottom_right(self):
        position1 = 'c8'
        position2_list = ['d7', 'e6', 'f5', 'g4', 'h3']
        for position2 in position2_list:
            result = is_align_diagonally(position1, position2)
            self.assertTrue(result, position2)

    def test_is_align_diagonally_towards_top_right(self):
        position1 = 'a1'
        position2_list = ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8']
        for position2 in position2_list:
            result = is_align_diagonally(position1, position2)
            self.assertTrue(result, position2)

    def test_c4_is_not_align_diagonally_with_itself(self):
        result = is_align_diagonally('c4', 'c4')
        self.assertFalse(result)

    def test_c4_is_not_align_diagonally_with_a1(self):
        result = is_align_diagonally('c4', 'a1')
        self.assertFalse(result)

    def test_b3_is_not_align_diagonally_with_a1(self):
        result = is_align_diagonally('b3', 'a1')

