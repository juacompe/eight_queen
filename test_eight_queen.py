#-*- coding: utf-8 -*-
from eight_queen import get_board, put_queen
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


def assertLikes(test, expected, result):
    """
    Assert that 2 strings are equal if the whitespace is ignored
    """
    test.assertEquals(expected.replace(' ', ''), result.replace(' ', ''))
