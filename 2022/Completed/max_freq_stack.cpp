#include<unordered_map>
#include<stack>
#include<assert.h>
#include<iostream>
using namespace std;

class FreqStack
{
    int high_ = 0;
    unordered_map<int, stack<int>> items_; // freq, items
    unordered_map<int, int> count_;        // item, count

public:
    // FreqStack(int high) :high_{high} {
    //     // Member initializer
    //     cout << high_;
    // }
    void push(int val)
    {
        int c = ++count_[val];
        high_ = max(high_, c); // update count & find most frequent
        items_[c].push(val);
    }

    int pop()
    {
        // assertion should not mutate the object
        assert(items_.count(high_) > 0);
        cout << high_ << endl;
        auto &high_stack = items_[high_];
        assert(!high_stack.empty());

        // duplicate code confusing
        // high_ might change, so we should reference
        int x = high_stack.top();

        // cout << "popped" << x << endl;
        high_stack.pop();
        count_[x]--;
        if (high_stack.empty())
        {
            high_--;
        }
        return x;
    }
};