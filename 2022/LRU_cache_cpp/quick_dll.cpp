#include "doubly_linked_list.h"

int main() {
    DLList L = DLList();
    for (int i=1; i<=10; i++) {
        L.push_back(i);
    }
    L.display();
    
}