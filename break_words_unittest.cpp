#include "gtest/gtest.h"
#include "break_words.h"
#include <string>
#include <unordered_set>
namespace
{
const std::string s1{"abc"}, s2{"cba"};
const std::unordered_set<std::string> words1{"abc"}, words2{"cba"}, words3;
TEST(BreakWords, OneWord) {
    ASSERT_TRUE(break_words(s1, words1));
    // ASSERT_TRUE(break_words(s2, words2));
}

// TEST(BreakWords, EmptyString) {
//     ASSERT_TRUE(break_words("",words1));
//     ASSERT_TRUE(break_words("",words2));
//     ASSERT_TRUE(break_words("",words3));
// }
// TEST(BreakWords, EmptyDict) {
//     ASSERT_TRUE(break_words("", words3));
//     ASSERT_TRUE(break_words(s1, words3));
//     ASSERT_TRUE(break_words(s2, words3));
// }

// const std::string s1{"ryango"}, s2{"desiccatesciencecomputeralgorithms"};
// const std::string s3{"ryanog"}, s4{"algorithmscience"};
// const std::unordered_set<std::string> dictionary{
//     "ryan", "go", "desiccate", "computer", "science", "algorithms"
// };
// TEST(BreakWords, EmptyString) {
//     ASSERT_TRUE(break_words("",words1));
//     ASSERT_TRUE(break_words("",words2));
//     ASSERT_TRUE(break_words("",words3));
// }
// TEST(BreakWords, EmptyDict) {
//     ASSERT_TRUE(break_words("", words3));
//     ASSERT_TRUE(break_words(s1, words3));
//     ASSERT_TRUE(break_words(s2, words3));
// }

// const std::string s1{"ryango"}, s2{"desiccatesciencecomputeralgorithms"};
// const std::string s3{"ryanog"}, s4{"algorithmscience"};
// const std::unordered_set<std::string> dictionary{
//     "ryan", "go", "desiccate", "computer", "science", "algorithms"
// };
// TEST(BreakWords, ActualWords) {
//     ASSERT_TRUE(break_words(s1, dictionary));
//     ASSERT_TRUE(break_words(s2, dictionary));
//     ASSERT_FALSE(break_words(s3, dictionary));
//     ASSERT_FALSE(break_words(s4, dictionary));
// }

// std::unordered_set<std::string> dictionary;
// const int N{20};
// for (int i = 0; i < 20; ++i) {
//     const std::string s = gen_random(N);
//     dictionary.insert(s);
// }

// TEST(BreakWords, RandomWords) {
//     for (const auto &element : dictionary) {
//         ASSERT_TRUE(break_words(element, dictionary));
//     }
// }

}