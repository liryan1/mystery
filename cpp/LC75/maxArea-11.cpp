#include "common_ds.h"

int getArea(vector<int>& height, int i, int j) {
  return min(height[i], height[j]) * abs(j - i);
}

int maxArea(vector<int>& height) {
  int area = 0;
  int beg = 0, end = height.size() - 1;

  while (beg < end) {
    area = max(area, getArea(height, beg, end));
    if (height[beg] > height[end]) {
      end--;
    } else {
      beg++;
    } 
  }

  return area;
}