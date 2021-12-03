import unittest

from src.day3 import calculate_gamma, calculate_commonest, check_bit

test_input = ['00100',
              '11110',
              '10110',
              '10111',
              '10101',
              '01111',
              '00111',
              '11100',
              '10000',
              '11001',
              '00010',
              '01010']


class Day3(unittest.TestCase):
    def test_calculate_gamma(self):
        gamma = calculate_gamma(test_input)
        self.assertEqual('10110', gamma)

    def test_calculate_oxygen(self):
        oxygen = check_bit(0, test_input, True)
        self.assertEqual('10111', oxygen)


if __name__ == '__main__':
    unittest.main()
