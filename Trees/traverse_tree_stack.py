'''
Traverse tree no recursion
'''
from DS.node import Node
from collections import deque

def Tstack(root:Node):
    if not root: return;
    stack = deque(root)
    while stack:
        x = stack.pop()
        print(x)
        if x.left:
            stack.append(x.left)
        if x.right:
            stack.append(x.right)
    