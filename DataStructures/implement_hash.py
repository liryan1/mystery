class MyHashMap:

    def __init__(self):
        self.m = 100000
        self.data = [None for _ in range(self.m)]

    def hash_func(self, key):
        return key % self.m

    def put(self, key: int, value: int) -> None:
        i = self.hash_func(key)
        if not self.data[i]:
            self.data[i] = Node((key, value))
            return
        self.data[i] = Node.insert(self.data[i], (key, value))

    def get(self, key: int) -> int:
        i = self.hash_func(key)
        node = self.data[i]
        if not node:
            return -1
        while node:
            if node and node.pair[0] == key:
                return node.pair[1]
        return -1

    def remove(self, key: int) -> None:
        i = self.hash_func(key)
        self.data[i] = Node.remove(self.data[i], key)


class Node:
    def __init__(self, pair):
        self.pair = pair
        self.next = None

    @staticmethod
    def insert(head, new_pair) -> 'Node':
        ''' Insert at the front.'''
        curr = head
        while curr:
            if curr and curr.pair[0] == new_pair[0]:
                curr.pair = new_pair
                return head
            curr = curr.next
        curr = Node(new_pair)
        curr.next = head
        return curr

    @staticmethod
    def remove(head, key) -> None:
        if not head:
            return
        if head.pair[0] == key:
            head = head.next
            return head
        prev = curr = head
        while curr:
            if curr.pair[0] == key:
                prev.next = curr.next
                return head
            prev, curr = curr, curr.next
        return head

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
