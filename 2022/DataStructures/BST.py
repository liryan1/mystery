'''
Binary Search Tree implementation.
'''
from collections import deque
from random import randrange, choice
import io


class Node:
    def __init__(self, data: int=0) -> None:
        self.val = data
        self.left = self.right = None

    def print_PO(self) -> str:
        '''Pre order print'''
        if self is None: return ""
        return " " + str(self.val) + Node.look(self.left) + Node.look(self.right)

    def display(self) -> str:
        ''' Prints a visual of the tree to console. Code is from:
            https://stackoverflow.com/questions/34012886
        '''
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self) -> str:
        """ https://stackoverflow.com/questions/34012886
        Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Tree:
    def __init__(self, data=None) -> None:
        ''' If data is Node instance, set root to data.
            If data is not iterable, set root to None.
            Else, construct the tree by inserting every element in data.
        '''
        if hasattr(data, 'val') and hasattr(data, 'left') and hasattr(data, 'right'):
            self.root = data
            return
        try:
            iter(data)
        except TypeError:
            self.root = None
        else:
            self.root = None
            for d in data:
                self.insert(d)
        return
        

    def layers(self):
        ''' Debug function to look through the tree per level with BFS '''
        if not self.root: return ""
        out = ""
        curr_lev = 0
        q = deque()
        q.appendleft((self.root, 0))
        while q:
            curr, lev = q.pop()
            if lev > curr_lev:
                curr_lev += 1
                out += "\n"
            out += f"\t{curr.val}"
            if curr.left:
                q.appendleft((curr.left, lev+1))
            if curr.right:
                q.appendleft((curr.right, lev+1))
        return out

    def insert(self, i: int) -> None:
        ''' Insert element into BST. '''
        def _insert(node, i):
            if node.val > i:
                if not node.left:
                    node.left = Node(i)
                else:
                    _insert(node.left, i)
            elif node.val < i:
                if not node.right:
                    node.right = Node(i)
                else:
                    _insert(node.right, i)
            else: # node value is the same as i
                print("Value already exists")

        if not self.root:
            self.root = Node(i)
        else:
            _insert(self.root, i)

    def delete(self, i: int) -> None:
        '''Delete the value and maintain valid BST.
        1. If not self.left or not self.right, then we just remove the non-empty node,
        then move the value up.
        2. Else, find value of the maximum on the left node 
        '''
        def _deleteNode(node: Node, i: int) -> Node:
            if not node: return None
            if node.val > i:
                node.left = _deleteNode(node.left, i)
            elif node.val < i:
                node.right = _deleteNode(node.right, i)
            else: # found the node to delete
                if not node.left or node.right:
                    return node.right or node.left
                # darn it, both nodes exist
                temp = node.left
                while temp.right:
                    temp = temp.right
                node.val = temp.val
                node.left = _deleteNode(node.left, node.val)
            return node

        self.root = _deleteNode(self.root, i)

    def __repr__(self) -> str:
        return self.root.display() if self.root else ""


class SerializeTree:
    def _serial_write(self, root, f: io.TextIOWrapper) -> None:
        if not root:
            f.write("R\n")
            return
        f.write(f"{root.val}\n")
        self._serial_write(root.left, f)
        self._serial_write(root.right, f)

    def serialize(self, root: 'Node', file_name: str = 'tree.txt') -> None:
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
