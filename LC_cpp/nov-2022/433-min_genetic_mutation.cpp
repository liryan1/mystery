#include "includes.h"

using namespace std;

// https://leetcode.com/problems/minimum-genetic-mutation/
class Solution {
private:
    // check possible changes by replacing current letter with ACGT
    void updateQ(queue<string> &q, string &curr, unordered_set<string> &set) {
        for (int i = 0; i < curr.length(); ++i) {
            string temp = curr;
            temp[i] = 'A';
            if (set.count(temp))
                q.push(temp);
            temp[i] = 'C';
            if (set.count(temp))
                q.push(temp);
            temp[i] = 'G';
            if (set.count(temp))
                q.push(temp);
            temp[i] = 'T';
            if (set.count(temp))
                q.push(temp);
        }
    }

public:
    int minMutation(string start, string end, vector<string>& bank) {
        unordered_set<string> set{bank.begin(), bank.end()};
        queue<string> Q;
        string curr;
        int steps = 0, iter = 0;
        
        if (!set.count(end))
            return -1;

        Q.push(start);
        while (!Q.empty()) {
            iter = Q.size();
            while (iter--) {
                curr = Q.front();
                Q.pop();
                if (curr == end) // found the answer
                    return steps;

                set.erase(curr); // erase the current to avoid redundant checking
                updateQ(Q, curr, set);
            }
            steps++;
        }
        return -1;
    }
};