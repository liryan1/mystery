''' Implementation moved to DS/node.py
'''

from DS.node import Node


def serialize(tree, root: Node) -> None:
    ''' Serialize tree using I/O.
    TODO: handle write error
    '''
    if not root:
        tree.write("X\\")
        return
    tree.write(f"{root.val}\\")
    serialize(tree, root.left)
    serialize(tree, root.right)


def build(tree_items: list) -> Node:
    ''' Reconstructs the tree from serialized list.
    TODO: Handle I/O errors, file stream
    '''
    if not tree_items:
        return

    def r(i):
        # Keeprint track of where we are in the array
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
    print("Initial tree (printre-order):")
    print(Node.look(root))

    print("Serialized Tree")
    with open("tree.txt", "w") as f:
        serialize(f, root)

    print("Reconstructed Tree")
    # pass in file into the tree
    # read in file stream and parse 
    with open("tree.txt", "r") as f:
        tree_str = f.read()
    tree = tree_str.split("\\")
    print(tree)

    recon = build(tree)
    print(Node.look(recon))
