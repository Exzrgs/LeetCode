"""
Question:
    How is the size of n?
Test:
    empty
    count > len(list)
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        if n == length:
            return head.next
        
        count = 1
        prev = None
        current = head
        while current and count < length - n + 1:
            prev = current
            current = current.next
            count += 1
        if n == 1:
            prev.next = None
        else:
            prev.next = current.next
        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        count = 0
        while count < n:
            right = right.next
            count += 1
        
        dummy = ListNode(val=-1, next=head)
        left = dummy
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
