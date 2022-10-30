#include<vector>
using namespace std;

// running sum from right to left
// [1,7,3,6,5,6]
// rsum = [28,27,20,17,11,6]
// total_sum
// loop from left, check for pivot
// current = 0
// if current == rsum[i] - nums[i]: return i
// else: current += nums[i], total_sum -= nums[i]

class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int sum = 0, curr = 0;
        for (auto &num : nums)
        {
            sum += num;
        }

        for (int i = 0; i < nums.size(); ++i)
        {
            curr += nums[i];
            if (curr == sum)
            {
                return i;
            }
            sum -= nums[i];
        }
        return -1;
    }
};