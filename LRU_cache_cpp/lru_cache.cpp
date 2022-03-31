#include <unordered_map>
#include <iostream>
#include "doubly_linked_list.h"
using namespace std;

/* Implementation of an LRU cache (least recently used)
Doubly linked list and track head and tail
*/


// class LRUCache
// {
// public:
//     LRUCache(int capacity)
//     {
//     }

//     int get(int key)
//     {
//     }

//     void put(int key, int value)
//     {
//     }
// };

int main() {
    DLList L = DLList();
    for (int i=1; i<=10; i++) {
        L.push_back(i);
    }
    L.display();
    
}