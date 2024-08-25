class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {None: None}
        current = head
        while current:
            original_to_copy[current] = Node(x=current.val)
            current = current.next
        
        current = head
        while current:
            copy = original_to_copy[current]
            copy.next = original_to_copy[current.next]
            copy.random = original_to_copy[current.random]
            current = current.next
        return original_to_copy[head]
