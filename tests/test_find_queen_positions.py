from eight_queen import find_queen_positions, find_safe_positions
from test_fixture import empty_board, board_with_queen_at_a1
from unittest import TestCase
from utils import all_positions

class TestFindQueenPositions(TestCase):
    def test_find_queen_positions_on_empty_board(self):
        queen_positions = find_queen_positions(empty_board)
        self.assertEquals([], queen_positions)

    def test_find_queen_positions_on_board_with_queen_at_a1(self):
        queen_positions = find_queen_positions(board_with_queen_at_a1)
        self.assertEquals(['a1'], queen_positions)

class TestFindSafePositions(TestCase):
    def test_all_positions_on_empty_board_is_safe(self):
        safe_positions = find_safe_positions([], all_positions)
        self.assertEquals(set(all_positions), set(safe_positions))

    def test_safe_positions_on_board_with_queen_at_a1(self):
        safe_positions = find_safe_positions(['a1'], all_positions)
        expected = [
            'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
            'c2', 'c4', 'c5', 'c6', 'c7', 'c8',
            'd2', 'd3', 'd5', 'd6', 'd7', 'd8',
            'e2', 'e3', 'e4', 'e6', 'e7', 'e8',
            'f2', 'f3', 'f4', 'f5', 'f7', 'f8',
            'g2', 'g3', 'g4', 'g5', 'g6', 'g8',
            'h2', 'h3', 'h4', 'h5', 'h6', 'h7',
        ] 
        self.assertEquals(set(expected), set(safe_positions))
        
    def test_safe_positions_on_board_with_4_queens_in_knight_pattern_starts_from_a1(self):
        queen_positions = ['a1', 'b3', 'c5', 'd7']
        safe_positions = find_safe_positions(queen_positions, all_positions)
        expected = [
            'e2', 'e4',
            'f4', 
            'g2', 'g6',
            'h2', 'h4', 'h6',
        ] 
        self.assertEquals(set(expected), set(safe_positions))
