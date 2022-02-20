'''
Given a binary tree, determine whether or not it is height-balanced. 
A height-balanced binary tree can be defined as one in which the heights 
of the two subtrees of any node never differ by more than one.
'''
from DS.node import Node


def is_balanced(root:Node) -> bool:
    def height(node:Node) -> int:
        if not node: return 0
        return 1 + max(height(node.left), height(node.right))

    return abs(height(root.left) - height(root.right)) <= 1