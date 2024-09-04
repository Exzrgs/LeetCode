# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(head):
            count = 0
            while head and count < k:
                head = head.next
                count += 1
            return head
        
        dummy = ListNode(next=head)
        group_prev = dummy
        while True:
            kth = get_kth(group_prev)
            if not kth:
                break
            group_next = kth.next
            
            cur = group_prev.next
            prev = group_next
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
        return dummy.next
