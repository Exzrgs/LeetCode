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
