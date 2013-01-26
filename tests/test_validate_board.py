#-*- coding: utf-8 -*-
from validate_board import validate_board, get_column, get_column_indexes
from test_fixture import empty_board
from unittest import TestCase

class TestValidateBoard(TestCase):
    def test_empty_board_should_valid(self):
        valid = validate_board(empty_board)
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
        #self.assertFalse(valid)


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
 
