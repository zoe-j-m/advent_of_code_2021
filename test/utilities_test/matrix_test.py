import unittest

from src.utilities.matrices import Matrix
from src.utilities.sliding_window import window


class MatrixTest(unittest.TestCase):
    def test_matrix_transpose(self):
        test_list = Matrix([[1, 2], [3, 4]])
        self.assertEqual([[1, 3], [2, 4]], test_list.transpose())

    def test_matrix_transpose2(self):
        test_list = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual([[1, 4], [2, 5], [3, 6]], test_list.transpose())

if __name__ == '__main__':
    unittest.main()
