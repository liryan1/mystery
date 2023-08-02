#include "common_ds.h"
using namespace std;

void backTrack(
  vector<vector<int>>& result,
  vector<int>& current,
  vector<int>& nums
) {
  if (current.size() == nums.size()) result.push_back(current);
  for (auto num: nums) {
    if (find(current.begin(), current.end(), num) == current.end()) {
      current.push_back(num);
      backTrack(result, current, nums);
      current.pop_back();
    }
  }
}

vector<vector<int>> permute(vector<int>& nums) {
  vector<vector<int>> result;
  vector<int> current;
  
  backTrack(result, current, nums);

  return result;
}