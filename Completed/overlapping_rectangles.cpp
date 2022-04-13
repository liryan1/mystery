// Given two sets of points representing rectangles, return whether they overlap.
#include <iostream>
#include <assert.h>
using namespace std;

struct Point {
    int x;
    int y;
};

struct Rect {
    Point BL;
    Point TR;
};

bool overlap(Rect &R1, Rect &R2)
{
    // Return True if they overlap.
    // TR: Top Right. BL: Bottom Left.
    // Coordinates for each rectangle: (x1, y1, x2, y2), 
    // where BL = (x1, y1), TR = (x2, y2)
    // Method: check both TR_x - BL_x > 0 && TR_y - BL_y > 0.
    // overlap iff both are true
    const bool check1 = (R2.TR.x - R1.BL.x > 0) && (R2.TR.y - R1.BL.y > 0);
    const bool check2 = (R1.TR.x - R2.BL.x > 0) && (R1.TR.y - R2.BL.y > 0);
    return check1 && check2;
}

int main() {
    Rect R1 = {{0, 0}, {2, 2}};
    Rect R2 = {{1, 1}, {3, 3}};
    assert(overlap(R1, R2) == true);
    cout << "----- Test1 passed." << endl;
    
    R1 = {{0, 0}, {1, 1}};
    R2 = {{1, 0}, {2, 1}};
    assert(overlap(R1, R2) == false);
    cout << "----- Test2 passed." << endl;

    R1 = {{0, 0}, {100, 1}};
    R2 = {{0, 1}, {100, 2}};
    assert(overlap(R1, R2) == false);
    cout << "----- Test3 passed." << endl;
}