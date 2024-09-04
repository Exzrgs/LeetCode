"""
Problem:
    separate list and each length is k
    reverse each segment
Question:
Discussion:
    define function to reverse segment
    def reverse_segment(head, length)

kthを取ってくることで、dummy.nextを正しく設定できている
"""
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse_list(head):
        cur = head
        prev = None
        count = 0
        while count < k:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            count += 1
        return prev, cur
    
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    count = 0
    prev_group_final = ListNode(next=head)
    group_final = head
    while length - count >= k:
        tmp, group_next = reverse_list(group_final)
        group_final.next = group_next
        group_final = group_next
        prev_group_final.next = tmp
        count += k
    return dummy.next
"""
これだと、dummy.nextが設定できない。reverseされたgroupのheadを持っていないから
dummy自体のポジションも動かしにくい。
"""

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
            
            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        return dummy.next            
