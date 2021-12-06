import unittest

from src.day3 import calculate_gamma, calculate_commonest, check_bit
from src.day4 import check_winner, find_winners
from src.day5 import extract_from_strings, coords_to_range, find_multi_visited_cells
from src.utilities.matrices import Matrix

test_input = ['0,9 -> 5,9',
              '8,0 -> 0,8',
              '9,4 -> 3,4',
              '2,2 -> 2,1',
              '7,0 -> 7,4',
              '6,4 -> 2,0',
              '0,9 -> 2,9',
              '3,4 -> 1,4',
              '0,0 -> 8,8',
              '5,5 -> 8,2']


class Day5Test(unittest.TestCase):
    def test_extract(self):
        extracts = extract_from_strings(test_input)
        self.assertEqual(((0, 9), (5, 9)), extracts[0])

    def test_coords(self):
        forward_test = ((0, 9), (5, 9))
        backward_test = ((5, 9), (1, 9))
        self.assertEqual([(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)], coords_to_range(forward_test))
        self.assertEqual([(5, 9), (4, 9), (3, 9), (2, 9), (1, 9)], coords_to_range(backward_test))

    def test_counts(self):
        extracts = extract_from_strings(test_input)
        horivertipaths = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], extracts))
        print(horivertipaths)
        paths = list(map(coords_to_range, horivertipaths))

        self.assertEqual(5, find_multi_visited_cells(paths))

    def test_counts2(self):
        extracts = extract_from_strings(test_input)
        paths = list(map(coords_to_range, extracts))

        self.assertEqual(12, find_multi_visited_cells(paths))


if __name__ == '__main__':
    unittest.main()
