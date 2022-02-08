from collections import deque

class Node:
    def __init__(self, data=0):
        self.val = data
        self.left = self.right = None

    @staticmethod
    def look(node) -> str:
        '''Pre order print'''
        if node is None: return ""
        return " " + str(node.val) + Node.look(node.left) + Node.look(node.right)

class Tree:
    def __init__(self, node: Node=None) -> None:
        self.root = node

    @classmethod
    def build(cls, tree_items: list) -> Node:
        ''' Reconstructs the tree from serialized list.
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
        return cls(root)

    def __repr__(self) -> str:
        return Node.look(self.root)

    def write(self) -> str:
        tree = []
        def serialize(tree: list, root: Node) -> None:
            ''' Serialize tree to list container.'''
            if not root:
                tree.append("X")
                return
            tree.append(root.val)
            serialize(tree, root.left)
            serialize(tree, root.right)
        serialize(tree, self.root)
        return tree

    def in_order(self) -> str:
        def _inorder(node: Node):
            if node is None: return "";
            return f"{_inorder(node.left)} {node.val}{_inorder(node.right)}"
        return _inorder(self.root)

    def post_order(self) -> str:
        def _post(node: Node):
            if node is None: return ""
            return f"{_post(node.left)}{_post(node.right)} {node.val}"
        return _post(self.root)

if __name__ == "__main__":
    S = [1, 2, 5, 10, 'X', 'X', 'X', 8, 'X', 'X', 3, 'X', 6, 'X', 'X']
    tree = Tree.build(S)
    print(tree)
    print(tree.in_order())
    print(tree.post_order())
