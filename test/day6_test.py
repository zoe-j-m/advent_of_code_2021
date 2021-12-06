import unittest
from collections import Counter
from src.day6 import total_fish, apply_days

test_input = [3, 4, 3, 1, 2]


class Day6Test(unittest.TestCase):
    def test_partone(self):
        start_days = Counter(test_input)
        end_days = apply_days(18, start_days)
        self.assertEqual(26, total_fish(end_days))

    def test_partone2(self):
        start_days = Counter(test_input)
        end_days = apply_days(80, start_days)
        self.assertEqual(5934, total_fish(end_days))


if __name__ == '__main__':
    unittest.main()
