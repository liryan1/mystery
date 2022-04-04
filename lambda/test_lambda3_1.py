import unittest
from lambda3_1 import solution

class testLambda3_1(unittest.TestCase):
    def test_example1(self):
        F, M = '4', '7'
        ans = 4
        self.assertEqual(ans, solution(F, M))
    def test_example2(self):
        F, M = '1', '2'
        ans = 1
        self.assertEqual(ans, solution(F, M))

    def test2(self):
        F, M = '4', '31'
        ans = 10
        self.assertEqual(ans, solution(F, M))
