#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <numeric>
using namespace std;

unordered_map<tuple<int, int>, int> lookup0;

// Only care about the difference
int partition0(vector<int> const &list, int s1, int s2, int i)
{
    if (i > list.size()) {
        return abs(s1 - s2);
    }
    tuple<int, int> key={i, s1};
    if (lookup0.find(key) == lookup0.end()) {
        lookup0[key] = min(partition0(list, s1 + list[i], s2, i + 1),
                           partition0(list, s1, s2 + list[i], i + 1));
    }
    return lookup0[key];
}

void main() {
    vector<int> test = {5, 7, 2, 1, 10, 6, 8};
    int diff = partition0(test, 0, 0, 0);
    cout << "Minimum sum of two lists: " << diff << endl;
}