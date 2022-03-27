import unittest
import random
import string
from longest_palindrome import longest_palindrome

'''
'a' -> 1
'aaaaaaaaaaaaa' -> 13
'AabB' -> 1
'aabbccdef' -> 7
'aabbccDDEE' -> 10
very long test case
random test case
'''

# def brute_LP(s: str) -> int:
#     pass

class TestLongestPalindrome(unittest.TestCase):
    def test_one_a(self):
        input = 'a'
        output = 1
        self.assertEqual(longest_palindrome(input), output)

    def test_lots_of_as(self):
        input = 'aaaaaaaaaaaaa'
        output = 13
        self.assertEqual(longest_palindrome(input), output)

    def test_multiple_single_chars(self):
        input = 'aabbccdef'
        output = 7
        self.assertEqual(longest_palindrome(input), output)

    def test_all_even(self):
        input = 'aabbccddee'
        output = 10
        self.assertEqual(longest_palindrome(input), output)

    def test_very_long(self):
        input = string.ascii_lowercase * 10000
        output = len(string.ascii_lowercase) * 10000
        self.assertEqual(longest_palindrome(input), output)

    # def test_random(self):
    #     input = ''
    #     for _ in range(1000):
    #         input += chr(random.randint(96, 96+26))
    #     output = brute_LP(input)
    #     self.assertEqual(longest_palindrome(input), output)
