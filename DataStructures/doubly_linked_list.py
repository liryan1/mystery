''' Doubly Linked List implementation of O(1) methods.
    Did not implement O(n) methods such as index insert and look up delete.
'''


class DLNode:
    def __init__(self, val: int = 0, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"DLNode: val={self.val}"


class DoublyLinkedList:
    ''' Front node always points to the dummy node. '''

    def __init__(self) -> None:
        self._dummy = DLNode()
        self.front: 'DLNode' = self._dummy
        self.back: 'DLNode' = self._dummy
        self.length: int = 0

    def __repr__(self) -> str:
        s = []
        pointer = self.front.next
        while pointer:
            s.append(str(pointer.val))
            pointer = pointer.next
        return " -> ".join(s) if s else "Empty"

    def push_front(self, new: 'DLNode') -> None:
        ''' Insert "val" at the beginning of the list. O(1) '''
        new.prev = self.front
        new.next = self.front.next
        self.front.next = new
        new.next.prev = new
        self.length += 1

    def push_back(self, new: 'DLNode') -> None:
        ''' Insert "val" at the end of the list. O(1) '''
        new.prev = self.back
        new.next = None
        self.back.next = new
        self.back = new
        self.length += 1

    def remove(self, node: 'DLNode') -> None:
        ''' Delete "node" from the list. O(1) '''
        if not node: return
        if node == self.back:
            self.back = self.back.prev
            self.back.next = None
        elif node == self.front.next:
            self.front.next = self.front.next.next
            self.front.next.prev = self.front
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1


def has_cycle(head: 'DLNode') -> bool:
    if not head or head.next:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def debug():
    ''' Some debugging prints '''
    L = DoublyLinkedList()
    for i in range(1, 11):
        L.push_back(DLNode(i))

    # # Test remove
    # x = L.front.next
    # for i in range(5):
    #     L.remove(x)
    #     x = x.next
    #     print("front, back:",L.front.next.val, L.back.val)
    #     print("Cycle?", has_cycle(L.front) or has_cycle(L.back))

    print("L:", L)
    print("length:", L.length)
    print("Cycle?", has_cycle(L.front) or has_cycle(L.back))

    N = L.front.next
    for _ in range(3):
        N = N.next
    print("Removing:", N.val)
    L.remove(N)
    print("L:", L)
    print("length:", L.length)
    print("Cycle?", has_cycle(L.front) or has_cycle(L.back))



if __name__ == "__main__":
    debug()
