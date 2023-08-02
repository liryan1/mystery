''' LRU Cache implementation (least recently used).
    Uses hash table for lookup and a doubly-linked list for insertion and deletion.
'''
from DataStructures.doubly_linked_list import DoublyLinkedList, DLNode


class LRU_Cache:
    def __init__(self, capacity: int) -> None:
        ''' Data stores the (value, DLNode) of the item'''
        self.data = {}
        self.capacity = capacity
        self._cache = DoublyLinkedList()

    def get(self, key: int) -> int:
        ''' Refresh usage, return value of the key. '''
        # Get the node if it exists.
        data = self.data.get(key)
        if not data:
            return -1
        # Remove the node and push it to the end of the cache.
        self._cache.remove(data[1])
        self._cache.push_back(data[1])
        return data[0]

    
    def put(self, key: int, val: int) -> None:
        ''' Insert the node into cache, remove LRU if over capacity.
        '''
        # Get the node and remove the node from the cache if it already exists
        if key in self.data:
            node = self.data[key][1]
            self._cache.remove(node)
        else:
            # if it does not exist, create the node
            node = DLNode(key)
        
        # (re)insert the node to the end (most recent) of the cache
        self._cache.push_back(node)

        # Put the key, value pair into the hash table
        self.data[key] = [val, node]

        # Remove the LRU if over capacity
        if self._cache.length > self.capacity:
            # front.next is the first node (see implementation details)
            # bye is the node to remove
            bye = self._cache.front.next
            self._cache.remove(bye)
            del self.data[bye.val]


def debug():
    ''' Some debugging prints '''
    lRUCache = LRU_Cache(2)
    print("Put 1, 1")
    lRUCache.put(1, 1)
    print(lRUCache._cache)
    print("Put 2, 2")
    lRUCache.put(2, 2)
    print(lRUCache._cache)
    print("get 1")
    print(lRUCache.get(1))
    print(lRUCache._cache)
    print("put 3, 3")
    lRUCache.put(3, 3)
    print(lRUCache._cache)
    print("get 2")
    print(lRUCache.get(2))
    print(lRUCache._cache)
    print("put 4, 4")
    lRUCache.put(4, 4)
    print(lRUCache._cache)
    print("get 1")
    print(lRUCache.get(1))
    print(lRUCache._cache)
    print("get 3")
    print(lRUCache.get(3))
    print(lRUCache._cache)
    print("get 4")
    print(lRUCache.get(4))
    print(lRUCache._cache)


if __name__ == "__main__":
    debug()