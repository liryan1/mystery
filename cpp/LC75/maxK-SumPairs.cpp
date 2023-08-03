#include "common_ds.h"

int maxOperations(vector<int>& nums, int k) {
  // wanted number -> set of index in nums
  unordered_map<int, unordered_set<int>> lookingFor;
  int operations = 0;

  for (int i = 0; i < nums.size(); ++i) {
    lookingFor[(k - nums[i])].insert(i);
  }

  for (int i = 0; i < nums.size(); ++i) {
    if (lookingFor.find(nums[i]) != lookingFor.end()) {
      unordered_set<int>& pool = lookingFor[nums[i]];
      // ignore the case if the same element doubled is equal to k
      if (pool.size() == 1 && pool.find(i) != pool.end()) continue;
      if (pool.size() > 0) {
        pool.erase(pool.begin());
        operations++;
      }
    }

  }

  return operations / 2;
}