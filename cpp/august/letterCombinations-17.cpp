#include "common_ds.h"

map<char, string> numberToLetters {
  { '2', "abc" },
  { '3', "def" },
  { '4', "ghi" },
  { '5', "jkl" },
  { '6', "mno" },
  { '7', "pqrs" },
  { '8', "tuv" },
  { '9', "wxyz" },
};

void backTrack(
  vector<string>& result,
  string& temp,
  string& digits,
  int curr_index
) {
  if (temp.size() == digits.size()) {
    result.push_back(temp);
    return;
  }
  for (auto letter: numberToLetters.at(digits[curr_index])) {
    temp.push_back(letter);
    backTrack(result, temp, digits, curr_index + 1);
    temp.pop_back();
  }
}

vector<string> letterCombinations(string digits) {
  vector<string> result;
  if (digits.empty()) return result;
  string temp;
  backTrack(result, temp, digits, 0);
  return result;
}