''' Instructions
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
''' Examples
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1

Input: s = "bb"
Output: 2
'''
''' Thoughts
1. look through and save all instances of the string - dict{char: count}
2. check dict. start with len(s). If more than one odd, minus 1. 
'''
'''Edge cases
'a' -> 1
'aaaaaaaaaaaaa' -> 13
'AabB' -> 1
'aabbccdef' -> 7
'aabbccDDEE' -> 10
'''


def longest_palindrome(s: str) -> int:
    ''' Time complexity: O(n)
        Space complexity: O(1) because s can only have letters, i.e. 52 possibilities
        where n is the length of s
    '''
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    longest = len(s)
    for count in counts.values():
        if count % 2 == 1:
            longest -= 1

    if len(s) > longest:
        longest += 1
    return longest


a = "aabbccddef"
print(longest_palindrome(a))