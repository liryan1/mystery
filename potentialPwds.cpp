#include "common_ds.h"

/**
 * From a long string, find all the potential passwords
 * 
 * potential password:
 * length between 6 and 10, at least 2 different letters and 2 different numbers
 * 
 * abcd123abcdefgh
 * 
 * abcd12
 * abcd123
 * abcd123a
 * abcd123ab
 * abcd123abc
 * bcd123abc
 * cd123abc
 * d123abc
 * 123abc
 * 123abcd
 * 123abcde
 * 123abcdef
 * 123abcdefg
 * ...
 */

int potentialPwds(const string& s) {
  unordered_map<int, unordered_map<char, int>> t;
  for (const auto& ch: s) {
    for (const auto& key: t) {
      // t[key] = 
    }
  }
  return 0;
}