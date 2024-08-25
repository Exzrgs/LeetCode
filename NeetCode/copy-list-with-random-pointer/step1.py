"""

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {}
        
        original_current = head
        dummy = Node(x=-1)
        copy_current = dummy
        while original_current:
            if original_current not in old_to_copy:
                old_to_copy[original_current] = Node(x=original_current.val)
            copy_current.next = old_to_copy[original_current]
            copy_current = copy_current.next
            
            if original_current.random:
                if original_current.random not in old_to_copy:
                    old_to_copy[original_current.random] = Node(x=original_current.random.val)
                copy_current.random = old_to_copy[original_current.random]
            original_current = original_current.next
        return dummy.next
