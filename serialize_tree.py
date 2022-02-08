class Node:
    def __init__(self, data=0):
        self.val = data
        self.left = self.right = None
    
def P(node: Node) -> str:
    '''Preorder print'''
    if node is None: return ""
    return " " + str(node.val) + P(node.left) + P(node.right)


def serialize(tree: list, root: Node) -> None:
    ''' Serialize tree to list container.
    '''
    if not root:
        tree.append("X")
        return
    tree.append(root.val)
    serialize(tree, root.left)
    serialize(tree, root.right)

def build(tree_items: list) -> Node:
    ''' Reconstructs the tree from serialized list.
    '''
    if not tree_items: return;

    def r(i):
        # Keep track of where we are in the array
        if i >= len(tree_items) or tree_items[i] == "X":
            return None, i
        # Assign value of current index to node
        node = Node(tree_items[i])
        node.left, i = r(i+1)
        node.right, i = r(i+1)
        return node, i

    root, _ = r(0)
    return root

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.left.right = Node(8)
    root.left.left.left = Node(10)
    root.right.right = Node(6)
    print("Initial tree (Pre-order):")
    print(P(root))

    print("Serialized Tree")
    tree = []
    serialize(tree, root)
    print(tree)

    print("Reconstructed Tree")
    recon = build(tree)
    print(P(recon))