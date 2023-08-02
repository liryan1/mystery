// If current value is -1, don't do anything
// If grid[i][j] == 1 (pointing right), if j+1 is out of bounds or pointing left, set current value to -1
// Similar & opposite logic with == -1

#include "includes.h"
using namespace std;

class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int m = grid.size(), n  = grid[0].size();
        vector<int> land(n, 0);
        for (int i = 0; i < n; ++i) {
            land[i] = i;
        }
        for (int j = 0; j < m; ++j) {
            // Check each ball at current level and update it
            for (int i = 0; i < n; ++i) {
                int curr_pos = land[i];
                if (curr_pos == -1) continue;
                if (grid[j][curr_pos] == 1) {
                    if (curr_pos == n - 1 || grid[j][curr_pos + 1] == -1) {
                        land[i] = -1;
                    } else {
                        land[i]++;
                    }
                } else {
                    // grid == -1
                    if (curr_pos == 0 || grid[j][curr_pos - 1] == 1) {
                        land[i] = -1;
                    } else {
                        land[i]--;
                    }
                }
            }
        }
        return land;
    }
};