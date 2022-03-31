#include <iostream>
#include "doubly_linked_list.h"

struct Node
{
    int data;
    struct Node *prev;
    struct Node *next;
};

class DLList
{
    Node *front;
    Node *back;

public:
    DLList()
    {
        front = NULL;
        back = NULL;
    }
    void push_back(int);
    void delete_node(Node *);
    void display();
    Node* get_front();
    Node* get_back();
};

/* Insert a node at the end of the Doubly Linked list*/
void DLList::push_back(int val)
{
    Node *temp = new Node();
    temp->data = val;
    temp->prev = back;
    temp->next = NULL; // Not required I think
    if (back == NULL)
    {
        front = temp;
    }
    else
    {
        back->next = temp;
    }
    back = temp;
}

/* Delete node "bye" from the Doubly Linked List */
void DLList::delete_node(Node *bye)
{
    if (bye == NULL)
    {
        return;
    }
    if (bye->prev == NULL)
    {
        front = bye->next;
        front->prev = NULL;
    }
    else if (bye->next == NULL)
    {
        back = bye->prev;
        back->next = NULL;
    }
    else
    {
        bye->next->prev = bye->prev;
        bye->prev->next = bye->next;
    }
    delete (bye);
}

void DLList::display()
{
    struct Node *pointer;
    pointer = front;
    while (pointer != NULL)
    {
        std::cout << pointer->data << " ";
        pointer = pointer->next;
    }
}