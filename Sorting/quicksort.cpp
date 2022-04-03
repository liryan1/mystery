#include <iostream>
#include <vector>
using namespace std;

/* Partition numbers and put all smaller than pivot in the left */
int partition(vector<int> &numbers, int beg, int end) {
    int pivot_idx = end;
    int left = beg;
    for (int i = beg; i < end; ++i)
    {
        if (numbers[i] <= numbers[pivot_idx])
            swap(numbers[i], numbers[left++]);
    }
    swap(numbers[left], numbers[end]);
    return left;
}

void r_quicksort(vector<int> &numbers, int beg, int end) {
    if (beg >= end)
        return;

    int pivot_index = partition(numbers, beg, end);
    r_quicksort(numbers, beg, pivot_index-1);
    r_quicksort(numbers, pivot_index+1, end);
}

void quicksort(vector<int> &numbers) {
    r_quicksort(numbers, 0, numbers.size() - 1);
}

int main() {
    cout << "Start program" << endl;
    vector<int> a = {1, 3, 5, 2, 6, 4, 8, -10, -15, -17, 20, 16, 9};
    cout << "Original array: " << endl;
    for (int i = 0; i < a.size(); i++)
    {
        cout << " " << a[i];
    }
    cout << endl;

    cout << "Running Quicksort" << endl;
    quicksort(a);

    cout << "Sorted array: " << endl;
    for (int i = 0; i < a.size(); i++)
    {
        cout << " " << a[i];
    }
    cout << endl;

    cout << "End program" << endl;
}