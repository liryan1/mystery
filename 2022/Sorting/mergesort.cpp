#include "mergesort.h"
#include <iostream>
#include <vector>


void merge(std::vector<int> &nums, int beg, int mid, int end)
{
    int start = 0, i = beg, j = mid + 1;
    int temp[end - beg + 1]; // extra space

    // Always add smaller number to temporary array
    while (i <= mid && j <= end) {
        if (nums[i] <= nums[j])
            temp[start++] = nums[i++];
        else
            temp[start++] = nums[j++];
    }

    // collect lefover elements
    while (i <= mid) {
        temp[start++] = nums[i++];
    }
    while (j <= end) {
        temp[start++] = nums[j++];
    }

    // Copy elements to new array
    for (int i = beg; i <= end; ++i) {
        nums[i] = temp[i - beg];
    }

}

void r_mergesort(std::vector<int> &nums, int beg, int end)
{
    if (beg < end) {
        int mid = beg + (end - beg) / 2;
        r_mergesort(nums, beg, mid);
        r_mergesort(nums, mid+1, end);
        merge(nums, beg, mid, end);
    }
}

void mergesort(std::vector<int> &nums)
{
    r_mergesort(nums, 0, nums.size() - 1);
}

std::vector<int> generate_random_vector(int size, int maximum=1000)
{
    std::vector<int> a(size, 0);
    for (int i = 0; i < size; i++) {
        a[i] = rand() % maximum + 1;
    }
    return a;
}