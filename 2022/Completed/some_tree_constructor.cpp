 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
private:
    TreeNode* constructor(vector<int>& nums, int beg, int end) {
        if (beg > end) {
            return nullptr;
        }
        auto high_ptr = std::max_element(nums.begin() + beg, nums.begin() + end + 1);
        int high = *high_ptr;
        TreeNode* node = new TreeNode(high);
        node->left = constructor(nums, beg, high_ptr - nums.begin() - 1);
        node->right = constructor(nums, high_ptr - nums.begin() + 1, end);
        return node;
    }
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return constructor(nums, 0, nums.size() - 1);
    }
};