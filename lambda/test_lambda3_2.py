import unittest
from lambda3_2 import solution


class testLambda3_1(unittest.TestCase):
    def test_example3(self):
        input = 3 # (1, 2)
        answer = 1
        self.assertEqual(answer, solution(input))

    def test_example4(self):
        input = 4 # (1, 3) !(2, 2) not allowed
        answer = 1
        self.assertEqual(answer, solution(input))

    def test_example5(self):
        input = 5 # (1, 4), (2, 3)
        answer = 2
        self.assertEqual(answer, solution(input))

    def test_example6(self):
        input = 6  # (1, 5), (2, 4), (1, 2, 3)
        answer = 3
        self.assertEqual(answer, solution(input))

    def test_example7(self):
        input = 7  # (1, 6), (2, 5), (3, 4), (1, 2, 4)
        answer = 4
        self.assertEqual(answer, solution(input))

    def test_example8(self):
        input = 8
        answer = 5
        self.assertEqual(answer, solution(input))

    def test_example9(self):
        input = 9
        answer = 7
        self.assertEqual(answer, solution(input))

    def test_example10(self):
        input = 10
        answer = 9
        self.assertEqual(answer, solution(input))

    def test_input1(self):
        input = 200
        answer = 487067745
        self.assertEqual(answer, solution(input))

    def test_input2(self):
        input = 3
        answer = 1
        self.assertEqual(answer, solution(input))
