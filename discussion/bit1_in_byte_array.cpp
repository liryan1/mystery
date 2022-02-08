#include <iostream>
#include <vector>
using namespace std;

int table[256];
int i;

int count_bit1(std::vector<int> arr) {
    int sum = 0;
    for (i=0; i<size(arr); i++) {
        sum += table[(int)arr[i]];
    }
    return sum;
}

int main() {
    for (int i = 0; i < 256; i++) {
        table[i] = (i & 1) + table[i / 2];
    }
    vector<int> arr;
    for (i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        arr[i] = i;
    }
    cout << "Number of bit-1s: " << count_bit1(arr) << endl;
}
