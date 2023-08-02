import unittest
from lambda2 import solution

'''
Input:
solution.solution([1, 2, 3, 4], 15)
Output:
    -1,-1

Input:
solution.solution([4, 3, 10, 2, 8], 12)
Output:
    2,3

-- Java cases --
Input:
Solution.solution({1, 2, 3, 4}, 15)
Output:
    -1,-1

Input:
Solution.solution({4, 3, 10, 2, 8}, 12)
Output:
    2,3
'''

class TestLambda2(unittest.TestCase):
    def test1_not_found(self):
        inputs = ([1, 2, 3, 4], 15)
        output = [-1, -1]
        self.assertEqual(solution(*inputs), output)

    def test2_regular(self):
        inputs = ([4, 3, 10, 2, 8], 12)
        output = [2, 3]
        self.assertEqual(solution(*inputs), output)

    def test3(self):
        inputs = ([4, 3, 5, 7, 8], 12)
        output = [0, 2]
        self.assertEqual(solution(*inputs), output)

    def test_regular(self):
        inputs = ([4], 4)
        output = [0, 0]
        self.assertEqual(solution(*inputs), output)
