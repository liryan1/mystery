
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
private:
    bool isIsomorphicSubset(string s, string t) {
        // Map contains char in s and what char should be in t
        unordered_map<char, char> seen;
        for (int i = 0; i < s.size(); ++i) {
            // seen this char before
            if (seen.find(s[i]) != seen.end()) {
                // if current char in t is not what it is supposed to be
                if (seen.at(s[i]) != t[i])
                    return false;
            } else {
                // not seen this char before, add maaping
                seen[s[i]] = t[i];
            }
        }
        return true;
    }

public:
    bool isIsomorphic(string s, string t) {
        return isIsomorphicSubset(s, t) && isIsomorphicSubset(t, s);
    }
};