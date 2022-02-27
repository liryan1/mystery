import unittest
from random import randrange
from binary_search import searchRange

class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        for i in range(5):
            self.assertEqual(searchRange([], i), [-1, -1])
    
    def test_one_element_exists(self):
        for i in range(5):
            self.assertEqual(searchRange([i], i), [0, 0])

    def test_one_element_not_in(self):
        for i in range(5):
            self.assertEqual(searchRange([i], i+1), [-1, -1])

    def test_two_elements_exists(self):
        actual = searchRange([2, 2], 2)
        expected = [0, 1]
        self.assertEqual(actual, expected)

    def test_two_elements_not_in(self):
        actual = searchRange([2, 2], 5)
        expected = [-1, -1]
        self.assertEqual(actual, expected)

    def test_repeated_elements(self):
        actual = searchRange([5]*100, 5)
        expected = [0, 99]
        self.assertEqual(actual, expected)
    
    def test_beginning(self):
        L = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]
        actual = searchRange(L, 1)
        expected = [0, 2]
        self.assertEqual(actual, expected)

    def test_end(self):
        L = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]
        actual = searchRange(L, 9)
        expected = [39, 42]
        self.assertEqual(actual, expected)

    def test_middle(self):
        L = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]
        actual = searchRange(L, 3)
        expected = [10, 11]
        self.assertEqual(actual, expected)

    def test_random1(self):
        L = [randrange(1, 10) for _ in range(1000)]
        L.sort()
        start = L.index(5)
        stop = len(L) - 1 - L[::-1].index(5)
        expected = [start, stop]
        self.assertEqual(searchRange(L, 5), expected)
