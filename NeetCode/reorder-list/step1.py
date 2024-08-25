"""
Question:
    How is the size of n?
    value of node can be duplicated?
Discussion:
    go to end node
    go from start and end until go through each other
Test Case:
    empty
    odd length
    even length

in-placeでやらないといけない
1 2 3 4 5
"""

# not in-place
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        nodes = []
        current_node = head
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next
        
        dummy = ListNode(val=-1)
        head = dummy
        left = 0
        right = len(nodes) - 1
        while left < right:
            head.next = nodes[left]
            head.next.next = nodes[right]
            head = head.next.next
            left += 1
            right -= 1
        if len(nodes) % 2 == 1:
            head.next = nodes[left]
            head = head.next
        head.next = None

# in-place
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        second = slow.next
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        second = prev
        while first and second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
