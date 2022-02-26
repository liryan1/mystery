'''
Binary Search Tree implementation.
'''
from collections import deque

class Node:
    def __init__(self, data=0):
        self.val = data
        self.left = self.right = None

    @staticmethod
    def print_PO(node) -> str:
        '''Pre order print'''
        if node is None: return ""
        return " " + str(node.val) + Node.look(node.left) + Node.look(node.right)


class Tree:
    def __init__(self, data=None) -> None:
        ''' If data is not iterable, set root to none.
        Construct the tree by inserting every element in data.
        '''
        self.root = None
        try:
            iter(data)
        except TypeError:
            return
        else:
            for i in data:
                self.insert(i)

    def look(self):
        '''Look through the tree per level '''
        if not self.root: return ""
        out = ""
        curr_lev = 0
        q = deque()
        q.appendleft((self.root, 0))
        while q:
            curr, lev = q.pop()
            if lev > curr_lev:
                curr_lev += 1
                out += "\n"
            out += f"\t{curr.val}"
            if curr.left:
                q.appendleft((curr.left, lev+1))
            if curr.right:
                q.appendleft((curr.right, lev+1))
        return out


    def insert(self, i):
        ''' Insert element into BST. '''
        def _insert(node, i):
            if node.val > i:
                if not node.left:
                    node.left = Node(i)
                else:
                    _insert(node.left, i)
            elif node.val < i:
                if not node.right:
                    node.right = Node(i)
                else:
                    _insert(node.right, i)
            else: # node value is the same as i
                print("Value already exists")

        if not self.root:
            self.root = Node(i)
        else:
            _insert(self.root, i)

    def delete(self, i):
        '''Delete the value and maintain valid BST.
        1. If not self.left or not self.right, then we just remove the non-empty node,
        then move the value up.
        2. Else, find value of the minimum on the right node 
        '''
        def _deleteNode(node, i):
            if not node: return None
        self.root = _deleteNode(self.root, i)

        

    def __repr__(self) -> str:
        return Node.look(self.root)

if __name__ == "__main__":
    tree = Tree([7,6,1,2,9,4,5,10, 12,3, 15])
    print(tree.look())