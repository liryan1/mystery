#include "common_ds.h"

int longestSubarray(vector<int>& nums) {
  // Sliding window O(nums.size())
  int longest = 0;
  int zeros = 0;
  int beg = 0;
  for (int end = 0; end < nums.size(); ++end) {
    zeros += nums[end] == 0;

    // Slide the left margin right until the range is valid again
    while (zeros > 1) {
      zeros -= nums[beg] == 0;
      beg++;
    }

    longest = max(longest, end - beg);
  }
  return longest;
}