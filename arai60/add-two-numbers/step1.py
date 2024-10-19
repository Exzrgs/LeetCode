'''
nextを作る位置を工夫しないと最後に余計なノードを作ってしまう
最後にc==1で繰り上がりを足さないといけないことに最初は気づいていたが、実装しているうちに忘れてしまっていた...
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        now = head
        
        c = 0
        while l1 and l2:
            s = (l1.val + l2.val + c)%10
            c = (l1.val + l2.val + c)//10
            now.next = ListNode(s)
            now = now.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = (l1.val + c)%10
            c = (l1.val + c)//10
            now.next = ListNode(s)
            now = now.next
            l1 = l1.next
        while l2:
            s = (l2.val + c)%10
            c = (l2.val + c)//10
            now.next = ListNode(s)
            now = now.next
            l2 = l2.next
        if c == 1:
            now.next = ListNode(1)
        return head.next
