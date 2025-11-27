#include "common_ds.h"

int bit1Count(int n, const vector<int>& lookup) {
  return (lookup[n & 0xff] + 
          lookup[(n >> 8) & 0xff] + 
          lookup[(n >> 16) & 0xff] + 
          lookup[n >> 24]);
}

vector<int> sortByBits(const vector<int>& arr) {
  vector<int> byteTableOnes(256, 0);
  for (size_t i = 0; i < 256; i++) {
    byteTableOnes[i] = (i & 1) + byteTableOnes[i / 2];
  }
  
  sort(arr.begin(), arr.end(), [&](const int& v1, const int& v2) {
    int countA = bit1Count(v1, byteTableOnes);
    int countB = bit1Count(v2, byteTableOnes);
    if (countA == countB) {
      return v1 < v2;
    }
    return countA < countB;
  });

  return arr;
}
