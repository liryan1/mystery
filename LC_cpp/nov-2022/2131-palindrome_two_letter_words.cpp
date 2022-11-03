#include "includes.h"

using namespace std;

// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
// if palindrome, then add 2, use hashset to store wanted "words"
// if the reverse exists in the set, pop it and add 2
// else, add it to the set
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        int longest = 0;
        int doubleLetterWord = 0;
        unordered_map<string, int> wanted;
        for (string word : words) {
            if (word[0] == word[1]) {
                if (wanted[word] > 0) {
                    doubleLetterWord--;
                    wanted[word]--;
                    longest += 4;
                } else {
                    wanted[word]++;
                    doubleLetterWord++;
                }
            } else {
                string rev = word;
                reverse(rev.begin(), rev.end());
                if (wanted[rev] > 0) {
                    longest += 4;
                    wanted[rev]--;
                } else {
                    wanted[word]++;
                }
            }
        }
        return doubleLetterWord > 0 ? longest + 2 : longest;
    }
};