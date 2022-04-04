#include <vector>
// #include <algorithm>

class Solution {
private:
    bool overlap(std::vector<int> &one, std::vector<int> &two) {
        return (one[1] >= two[0] && two[1] >= one[0]);
    }
    std::vector<int> get_overlap(std::vector<int> &one, std::vector<int> &two) {
        return std::vector<int>
        {
            std::max(one.front(), two.front()),
            std::min(one.back(), two.back())
        };
    }
public:
    std::vector<std::vector<int>> intervalIntersection(std::vector<std::vector<int>> &firstList, std::vector<std::vector<int>> &secondList)
    {
        std::vector<std::vector<int>> results;
        int i = 0, j = 0;
        while (i < firstList.size() && j < secondList.size()) {
            auto &L1 = firstList[i];
            auto &L2 = secondList[j];
            if (overlap(L1, L2)) {
                results.push_back(get_overlap(L1, L2));
                if (L1[1] > L2[1]) {
                    L1[0] = std::max(L1[0], L2[0]);
                    j++;
                }
                else if (L1[1] < L2[1]) {
                    L2[0] = std::max(L1[0], L2[0]);
                    i++;
                }
                else {
                    i++;
                    j++;
                }
            }
            else {
                if (L1[1] < L2[1]) {
                    i++;
                }
                else {
                    j++;
                }
            }
        }
        return results;
    }
};

int main() {

}