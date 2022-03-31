#include <iostream>
struct Node
{
    int data;
    struct Node *prev;
    struct Node *next;
};

class DLList
{
private:
    Node *front;
    Node *back;

public:
    void push_back(int);
    void delete_node(Node *);
    void display();
    Node* get_front();
    Node* get_back();
};