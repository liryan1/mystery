''' Leetcode "Rotate Digits"
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

'''


class Solution:
    mapping = {"1": "1", "2": "5", "5": "2", "6": "9",
               "9": "6", "0": "0", "8": "8"}

    def is_valid(self, digits):
        flipped = ""
        for d in digits:
            if d not in Solution.mapping:
                return False
            flipped += Solution.mapping[d]
        return flipped != digits

    def get_digits(self, n):
        digits = []
        while n > 0:
            digits.append(str(n % 10))
            n //= 10
        return "".join(digits)

    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            if self.is_valid(self.get_digits(i)):
                ans += 1
        return ans