#include "common_ds.h"

int largestAltitude(vector<int>& gain) {
  int current_height = 0;
  int highest = 0;
  for (auto& change: gain) {
    current_height += change;
    highest = max(highest, current_height);
  }
  return highest;
}