'''
意識したこと
・fake_headを作る必要性
確認したこと
・各ポインタをちゃんと次のステップへ移動させているか?
・l1やl2が空のときにしっかりと動くか?
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(-1)
        tail = fake_head

        carry = 0
        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            carry = sum_val//10
            tail.next = ListNode(sum_val%10)
            tail = tail.next

        return fake_head.next