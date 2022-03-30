// Given two sets of points representing rectangles, return whether they overlap.
// R1:
#include <vector>
#include <iostream>
#include <assert.h>
using namespace std;

bool overlap(vector<int> &R1, vector<int> &R2)
{
    // Return True if they overlap.
    // TR: Top Right. BL: Bottom Left.
    // Coordinates for each rectangle: (x1, y1, x2, y2), 
    // where BL = (x1, y1), TR = (x2, y2)
    // Method: check both TR_x - BL_x > 0 && TR_y - BL_y > 0.
    // overlap iff both are true
    const bool check1 = (R2[2] - R1[0] > 0) && (R2[3] - R1[1] > 0);
    const bool check2 = (R1[2] - R2[0] > 0) && (R1[3] - R2[1] > 0);
    return check1 && check2;
}

int main() {
    vector<int> R1 = {0, 0, 2, 2};
    vector<int> R2 = {1, 1, 3, 3};
    assert(overlap(R1, R2) == true);
    cout << "----- Test1 passed." << endl;
    
    R1 = {0, 0, 1, 1};
    R2 = {1, 0, 2, 1};
    assert(overlap(R1, R2) == false);
    cout << "----- Test2 passed." << endl;

    R1 = {0, 0, 100, 1};
    R2 = {0, 1, 100, 2};
    assert(overlap(R1, R2) == false);
    cout << "----- Test3 passed." << endl;
}