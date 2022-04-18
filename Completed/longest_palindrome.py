''' Given a string s, find and return the longest contiguous substring of s that is a palindrome.
    
    Key point for sliding window: omit checking larger subsets if smaller already fails condition.
'''

def longestPalindrome(s: str) -> str:
    ''' Classic sliding window algorithm with O(n^2) time and O(n) space. '''
    n: int = len(s)
    longest_start = longest_len = 0 # track the longest

    for i in range(n):
        right = i
        # Check consecutive same characters and use as starting point
        while right + 1 < n and s[right] == s[right+1]:
            right += 1

        left = i
        # expand both ways if palindrome exists
        while left > 0 and right + 1 < n and s[left-1] == s[right+1]:
            left -= 1
            right += 1

        # Update the longest seen so far
        L = right - left + 1
        if L > longest_len:
            longest_start = left
            longest_len = L

    return s[longest_start:longest_start+longest_len]
