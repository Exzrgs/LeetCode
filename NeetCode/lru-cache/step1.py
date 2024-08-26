"""
Discussion:
    cache:
        hash map
        key -> (value, current_count)
        store value and current count
    count:
        int
        unique key count
    key_count_queue:
        deque
        push (key, current_count)
    
    you can know queue contains only one key by comparing queue count and cache count
    when we put, we update the cache count

なるほど～～～
LinkedListで表現すれば削除できるのか
"""

from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.key_count = 0
        self.time = 0
        self.used_times = deque()

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.cache:
            self.used_times.append((key, self.time))
            self.cache[key][1] = self.time
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key not in self.cache:
            self.key_count += 1
            if self.key_count == self.capacity:
                while True:
                    k, t = self.used_times.popleft()
                    if self.cache[k][1] == t:
                        del self.cache[k]
                        self.key_count -= 1
                        break
        self.used_times.append((key, self.time))
        self.cache[key] = [value, self.time]
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import deque

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        # headとtailを定義してるので、前と後ろは必ずある
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
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
        return
