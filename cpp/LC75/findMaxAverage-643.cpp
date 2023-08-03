#include "common_ds.h"

double findMaxAverage(vector<int>& nums, int k) {
  int maxAverage = INT_MIN;
  int sum = 0;

  for (int i = 0; i < nums.size(); ++i) {
    if (i < k) {
      sum += nums[i];
    } else {
      maxAverage = max(maxAverage, sum);
      sum += (nums[i] - nums[i - k]);
    }
  }
  return max(sum, maxAverage) / (double)k;
}