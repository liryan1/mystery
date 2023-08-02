#include "break_words.h"
#include <string>
#include <vector>
#include <unordered_set>

// wordDict: vector of string representing dictionary of valid words
// s: a string of letters to break down
// Returns true if s can be divided into valid words in dictionary.
bool break_words(const std::string &s, const std::unordered_set<std::string> &dictionary)
{
    if (dictionary.empty()) {
        return false;
    }
    const int n = s.length();
    std::vector<bool> table(n+1, false); // empty string is in any dictionary
    table[0] = true; // took ages to find this bug...
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            const std::string subtring = s.substr(j, i - j);
            if (table[j] && dictionary.find(subtring) != dictionary.end())
            {
                table[i] = true;
                break; // early break, already found it
            }
        }
    }
    return table.back();
}

// Generate random string of length len
// https://stackoverflow.com/questions/440133
std::string gen_random(const int len)
{
    static const char alphanum[] =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";
    std::string tmp_s;
    tmp_s.reserve(len);

    for (int i = 0; i < len; ++i)
    {
        tmp_s += alphanum[rand() % (sizeof(alphanum) - 1)];
    }
    return tmp_s;
}