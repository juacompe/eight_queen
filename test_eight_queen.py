#-*- coding: utf-8 -*-
from eight_queen import get_board, put_queen, validate_board, get_column, get_column_indexes
from unittest import TestCase

empty_board = u"""
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
class TestDisplay(TestCase):
    def test_get_empty_board(self):
        board = [] 
        result = get_board(board) 
        assertLikes(self, empty_board, result)

    def test_get_board_with_a_queen_at_a1(self):
        board = ['a1'] 
        result = get_board(board)
        expected = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        4 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ♛ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        """
        assertLikes(self, expected, result)

    def test_get_board_with_3_queens_at_a1_b3_and_c5(self):
        board = ['a1', 'b3', 'c5'] 
        result = get_board(board)
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
        expected = u"""
          a b c d e f g h
        8 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        7 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        6 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        5 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        4 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        3 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        2 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
        1 ♛ ◻ ◼ ◻ ◼ ◻ ◼ ◻
        """
        assertLikes(self, expected, result)

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
  
def assertLikes(test, expected, result):
    """
    Assert that 2 strings are equal if the whitespace is ignored
    """
    test.assertEquals(expected.replace(' ', ''), result.replace(' ', ''))