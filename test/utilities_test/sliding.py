import unittest

from src.utilities.sliding_window import window


class Sliding(unittest.TestCase):
    def test_slidingwindow(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual([[1, 2], [2, 3], [3, 4]], window(2, test_list) )


    def test_slidingwindow3(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual([[1,2,3], [2,3,4]], window(3, test_list))


if __name__ == '__main__':
    unittest.main()
