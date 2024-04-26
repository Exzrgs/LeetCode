'''
変数名をfake_head→dummy
%の両端にspace
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy

        carry = 0
        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            carry = sum_val // 10
            tail.next = ListNode(sum_val % 10)
            tail = tail.next

        return dummy.next
