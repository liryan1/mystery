'''
Traverse a tree using O(1) space with a parent node.
'''
from DS.node import Node2

def traverse(root: Node2):
    back = None
    curr = root
    # stop if back to root and coming from right
    while curr:
        if back == curr.parent: # First time through
            print(curr.val)
            back = curr
            if curr.left:
                curr = curr.left
            elif curr.right:
                curr = curr.right
            else:
                curr = curr.parent
        elif back == curr.left: # coming from the left node
            back = curr
            if curr.right:
                curr = curr.right
            else:
                curr = curr.parent
        else: # coming up from right node
            back = curr
            curr = curr.parent

