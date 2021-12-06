import unittest

from src.day3 import calculate_gamma, calculate_commonest, check_bit
from src.day4 import check_winner, find_winners
from src.utilities.matrices import Matrix

test_input = [[1, 2], [3, 4]]
test_input2 = [[1, 5], [3, 4]]



class Day4(unittest.TestCase):
    def test_no_winner(self):
        is_winner = check_winner(Matrix(test_input), {1})
        self.assertFalse(is_winner)

    def test_row_winner(self):
        is_winner = check_winner(Matrix(test_input), {2, 1})
        self.assertTrue(is_winner)

    def test_col_winner(self):
        is_winner = check_winner(Matrix(test_input), {3, 1})
        self.assertTrue(is_winner)

    def test_winner_set(self):
        winners = [2,1,5]
        board = Matrix(test_input)
        board2 = Matrix(test_input2)
        winning_board = find_winners(winners, [board, board2], 1)[0]
        self.assertEqual(winning_board.rows, test_input)

    def test_winner_set2(self):
        winners = [1,5, 2]
        board = Matrix(test_input)
        board2 = Matrix(test_input2)
        winning_board = find_winners(winners, [board, board2], 1)[0]
        self.assertEqual(winning_board.rows, test_input2)


if __name__ == '__main__':
    unittest.main()
