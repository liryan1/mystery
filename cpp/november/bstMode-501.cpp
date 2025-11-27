#include "common_ds.h"

void inorder(const TreeNode* node, unordered_map<int, int>& tally) {
  if (node == nullptr) return;
  tally[node->val]++;
  inorder(node->left, tally);
  inorder(node->right, tally);
}

vector<int> findMode(const TreeNode* root) {
  unordered_map<int, int> tally;
  inorder(root, tally);
  
  int max_count = 0;
  for (const auto& kv: tally) {
    max_count = max(max_count, kv.second);
  }

  vector<int> modes;
  for (const auto& kv: tally) {
    if (kv.second == max_count) {
      modes.push_back(kv.first);
    }
  }

  return modes;
}