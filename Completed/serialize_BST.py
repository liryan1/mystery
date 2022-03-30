from DataStructures.BST import Node, Tree
from random import randrange
import io


class SerializeTree:
    ''' Second attempt at given task. Also a leetcode hard. '''

    def _serial_write(self, root, f: io.TextIOWrapper) -> None:
        if not root:
            f.write("R\n")
            return
        f.write(f"{root.val}\n")
        self._serial_write(root.left, f)
        self._serial_write(root.right, f)
        

    def serialize(self, root: 'Node', file_name: str='tree.txt') -> None:
        """ Encodes a tree to a file.
            'R' are empty branches, '\n' are delimitors.
        """
        with open(file_name, 'w') as f:
            self._serial_write(root, f)


    def _make_node(self, s: str) -> 'Node':
        ''' Create a Node if s is convertible to integer. '''
        s = s.rstrip("\n")
        if not s.isnumeric():
            return None
        return Node(int(s))


    def _dfs(self, f: io.TextIOWrapper) -> 'Node':
        ''' Helper function for in order traversal'''
        node = self._make_node(f.readline())
        if not node:
            return
        node.left = self._dfs(f)
        node.right = self._dfs(f)
        return node


    def deserialize(self, path_to_file: str) -> 'Node':
        """Decodes your encoded data to tree.
        """

        with open(path_to_file, 'r') as f:
            node = self._dfs(f)
        return node


def main():
    # Random test
    filename = "tree.txt"
    tree = Tree()
    for _ in range(10):
        x = randrange(1, 100)
        tree.insert(x)
    print("Original Tree\n", tree, sep="")
    print(f"Serializing Tree to {filename}")
    S = SerializeTree()
    S.serialize(tree.root, filename)
    print("Done")
    print("Deserializing Tree")
    new_tree = Tree(S.deserialize(filename))
    print("Done")
    print("New Tree\n", new_tree, sep="")


if __name__ == "__main__":
    main()
    