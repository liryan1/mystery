from Completed.Trees.node import Node, Tree

def post_from_IP(inO: list[int], preO: list[int]) -> Node:
    ''' Get post-order traversal from in-order and pre-order.
    '''
    if not inO: return
    idx = inO.index(preO.pop(0))
    node = Node(inO[idx])
    node.left = post_from_IP(inO[:idx], preO)
    node.right = post_from_IP(inO[idx+1:], preO)
    return node


def main():
    S = [1, 2, 5, 10, 'X', 'X', 'X', 8, 'X', 'X', 3, 'X', 6, 'X', 'X']
    tree = Tree.build(S)
    preO = repr(tree).strip().split(" ")
    IO = tree.in_order().strip().split(" ")
    print("Original preorder:", preO)
    print("Original inorder", IO)
    recon = post_from_IP(IO, preO)
    print("Reconstructed preorder", Node.look(recon))

if __name__ == "__main__":
    main()
