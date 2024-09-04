"""
Question:
    How is the size of k?
        0 <= k <= 10^4
    How is the lenght of each linked-list?
        0 <= length <= 500

LinkedListに対しても、どういうときにdummyを持ちたいかどうかを考えたほうがよさそう
メリット
・headを指しやすい
    これは、mergeのときとかは特に顕著。どっちがheadになるかわからないので
    しかも、headがNoneになるときもうまく返せる
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def print_linked_list(ls):
            res = []
            cur = ls
            while cur:
                res.append(cur.val)
                cur = cur.next
            print(res)
        
        def merge_list(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next
            
        
        if len(lists) == 0:
            return None
        merged = lists[0]
        for i in range(1, len(lists)):
            merged = merge_list(merged, lists[i])
        return merged
