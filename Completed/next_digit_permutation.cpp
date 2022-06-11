#include<string>
#include<algorithm>
using namespace std;

class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        int i = s.size() - 2;
        
        // next permutation algorithm
        for(; i >= 0; i--) {
            if(s[i] < s[i + 1]) {
                break;
            }
        }
        if(i < 0) {
            return -1;
        }
        
        // find the number right of i just greater than i
        for(int j = s.size() - 1; j > i; j--){
            if(s[j] > s[i]) {
                swap(s[i], s[j]);
                break;
            }
        }
        
        // reverse everything right of i
        reverse(s.begin() + i + 1, s.end());
        long res = stol(s); // convert back to integer
        
        // make sure within 32-bits
        return res > INT_MAX? -1 : res; 
    }
};