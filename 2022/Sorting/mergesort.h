#ifndef __MERGESORT_H_
#define __MERGESORT_H_
#include <vector>

// Merge 2 sorted subarrays of nums: (1) nums[beg:mid+1] (2) nums[mid:end+1]
// uses O(n) extra space
void mergesort(std::vector<int> &nums);

// Generate a vector of random integers of size and range
std::vector<int> generate_random_vector(int size, int maximum=1000);

#endif