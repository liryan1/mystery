#include "common_ds.h"

unordered_set<char> vowels = { 'a', 'e', 'i', 'o', 'u' };

int maxVowels(string s, int k) {
  int highest = INT_MIN;
  int current_vowels = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (i < k) {
      current_vowels += vowels.find(s[i]) != vowels.end();
    } else {
      highest = max(highest, current_vowels);
      current_vowels += vowels.find(s[i]) != vowels.end();
      current_vowels -= vowels.find(s[i - k]) != vowels.end();
    }
  }

  return max(highest, current_vowels);
}

// int main(int argc, char const *argv[])
// {
//   cout << maxVowels("abcdefg", 3) << endl;
//   return 0;
// }
