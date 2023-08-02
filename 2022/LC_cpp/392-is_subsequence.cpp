#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (t.empty() || s.empty())
            return true;
        int indS = 0, indT = 0, lenS = s.size();
        for (; indT < t.size(); ++indT) {
            if (t[indT] == s[indS]) {
                indS++;
            }
            if (indS == lenS) {
                return true;
            }
        }
        return false;
    }
};