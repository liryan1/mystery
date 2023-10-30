#include "common_ds.h"

int pivotIndex(vector<int>& nums) {
  vector<int> rightSum(nums.size(), 0);
  int sum = 0;
  for (int i = nums.size() - 1; i >= 0; --i) {
    rightSum[i] = sum;
    sum += nums[i];
  }

  sum = 0;
  for (int i = 0; i < nums.size(); ++i) {
    if (sum == rightSum[i]) {
      return i;
    }
    sum += nums[i];
  }

  return -1;
}