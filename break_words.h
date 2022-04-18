#ifndef BREAK_WORDS_H_
#define BREAK_WORDS_H_
#include <string>
#include <vector>
#include <unordered_set>
bool break_words(const std::string& s, const std::unordered_set<std::string>& dictionary);
std::string gen_random(const int len);
#endif