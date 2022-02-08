from DS.node import Node, Tree

S = [1, 2, 5, 10, 'X', 'X', 'X', 8, 'X', 'X', 3, 'X', 6, 'X', 'X']
tree = Tree.build(S)
print(tree)
print(tree.in_order())
print(tree.post_order())