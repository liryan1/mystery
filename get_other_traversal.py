from Trees.node import Node, Tree

def post_from_IP(InO: list[int], preO: list[int]) -> Node:
    ''' Get post-order traversal from in-order and pre-order.
    Assumes nodes have unique values
    '''
    if not preO: return;
    def _recursive(i:int, left:int, right:int):
        if i >= n or (left >= right): return None, i
        node = Node(preO[i])
        j = InO[left:right].index(preO[i]) + left
        node.left, i = _recursive(i+1, left, j)
        node.right, i = _recursive(i+1, j+1, right)
        return node, i

    n = len(preO)
    root, _ = _recursive(0, 0, n)
    return root


if __name__ == "__main__":
    S = [1, 2, 5, 10, 'X', 'X', 'X', 8, 'X', 'X', 3, 'X', 6, 'X', 'X']
    tree = Tree.build(S)
    preO = repr(tree).strip().split(" ")
    IO = tree.in_order().strip().split(" ")
    print(preO)
    print(IO)
    recon = post_from_IP(IO, preO)
    print(Node.look(recon))
