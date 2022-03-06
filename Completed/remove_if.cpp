#include <vector>
using namespace std;

bool criteria(int x) {
    return (x > 10);
}

void remove_if(std::vector<int> &arr) {
    // Keep track of good elements
    int good = 0;
    for (int i = 0; i < size(arr); i++) {
        if (criteria(arr[i])) {
            if (i != good) {
                arr[good] = arr[i];
            }
            good++;
        }
    }
    arr.resize(good);
}

