#include "common_ds.h"

void dfs(
  const unordered_map<int,
  vector<int>>& pairs,
  int current,
  unordered_set<int>& visited,
  vector<int>& array
) {
  if (visited.find(current) != visited.end()) {
    return;
  }
  array.push_back(current);
  visited.insert(current);
  for (auto num: pairs.at(current)) {
    dfs(pairs, num, visited, array);
  }
}

vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
  unordered_set<int> edge;
  vector<int> array;
  unordered_map<int, vector<int>> pairs;

  for (const auto& pair: adjacentPairs) {
      pairs[pair[0]].push_back(pair[1]);
      pairs[pair[1]].push_back(pair[0]);
      // find the edges
      for (const auto& num: pair) {
          if (edge.find(num) != edge.end()) {
              edge.insert(num);
          } else {
              edge.erase(num);
          }
      }
  }
  unordered_set<int> visited;
  dfs(pairs, *edge.begin(), visited, array);

  return array;
}