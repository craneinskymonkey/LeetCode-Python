import unittest
from leetcode.algorithms.p0073_set_matrix_zeroes_1 import Solution


class TestSetMatrixZeroes(unittest.TestCase):
    def test_set_matrix_zeroes(self):
        solution = Solution()
        actual_lists = [
          [1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]
        ]
        actual_lists2 = []
        expected_lists = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        solution.setZeroes(actual_lists)
        solution.setZeroes(actual_lists2)

        self.assertListEqual(expected_lists, actual_lists)
        self.assertListEqual([], actual_lists2)
