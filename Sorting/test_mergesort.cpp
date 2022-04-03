#include "mergesort.h"
#include <gtest/gtest.h>
#include <vector>

namespace {
TEST(TestMergesort, SameElements) {
    std::vector<int> a(100, 1);
    std::vector<int> b(a);
    mergesort(a);
    EXPECT_EQ(a, b) << "Sort error on identical elements ";
}
TEST(TestMergesort, randomElements) {
    for (int i = 0; i < 5; ++i) {
        std::vector<int> a = generate_random_vector(1000, 10000);
        std::vector<int> b(a);
        mergesort(a);
        sort(b.begin(), b.end());
        EXPECT_EQ(a, b) << "Sort failed on random elements" ;
    }
}
}