'''
List of strings, all strings equal length

return True if at least one pair of string has hamming distance of exactly 1

["abc", "acb", "xyz", "abd"] -> True
["abc", "abc", "abc"] -> False

N: length of strings, k: length of each string
k << N

"abc"
table {index: {character}}

"[!a]bc", "a[!b]c", "ab[!c]"
[a-z]
table = {bbc, cbc, dbc, ...
         aca, acc, adc, ...,
         aba, abb, abd, ...}
not the same lookup

(prefix, suffix): {"a", "b", "c"}
{prefix: {""}, suffixes: {"bc"}}, {prefix: {"a"}, suffix: {"c}}, {prefix: {"ab"}, suffix: {""}}


""

if we find the first character is different, we look inside a seen set

if we find the character is the same,

"a" "bc"

follow up: count hamming distance 1 pairs?


XOR hash can reduce to O(nk)
'''


def hamming_one(strings: list[str]) -> bool:
    lookup = {}
    for s in strings:
        for i in range(len(s)):
            pref_suf = (s[:i], s[i+1:])
            if pref_suf in lookup:
                if lookup[pref_suf] != s[i]:
                    return True
            else:
                lookup[pref_suf] = s[i]
    return False

def is_hamming_one(s1: str, s2: str) -> bool:
    '''Check two strings of the same length if the hamming distance is 1'''
    difference = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            difference += 1
        if difference > 1:
            return False

    return difference == 1

def hamming_one(strings: list[str]) -> bool:
    n = len(strings)
    for i in range(n-1):
        for j in range(i+1, n):
            if is_hamming_one(strings[i], strings[j]):
                return True
    return False

