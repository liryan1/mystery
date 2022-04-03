// showcasing memory allocation, potential leakage, and garbage collection
#include <iostream>

class vect {
    int *p_ = nullptr;
public:
    void set(int x) {
        if (p_ == nullptr) {
            // allocates new memory for int
            // stays until you manually delete it
            // 
            p_ = new int;
        }
        *p_ = x;
    }
    ~vect() {
        std::cout << "delete\n" << std::endl;
        delete p_;
    }
};

int main(int argc, char **argv) {
    {
    vect v;
    v.set(5);
    }
    std::cout << "done\n" << std::endl;
    return 0;
}

class X {
    vect* v;
    X() {
        v = new vect;
        v->set(5);
    }
    ~X() {
        delete v;
    }
};
