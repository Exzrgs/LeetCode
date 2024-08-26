class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert(self, node):
        prev, next = self.tail.prev, self.tail
        node.prev, prev.next = prev, node
        next.prev, node.next = node, next
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
