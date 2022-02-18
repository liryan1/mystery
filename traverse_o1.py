'''
Traverse a tree using O(1) space with a parent node.
'''
from DS.node import Node2

def traverse(root: Node2):
    back = None
    curr = root
    # stop if back to root and coming from right
    while curr:
        back = curr
        if back == curr.parent: # First time through
            print(curr.val)
            if curr.left:
                curr = curr.left
            elif curr.right:
                curr = curr.right
            else:
                curr = curr.parent
        elif back == curr.left: # coming from the left node
            if curr.right:
                curr = curr.right
            else:
                curr = curr.parent
        else: # coming up from right node
            curr = curr.parent

