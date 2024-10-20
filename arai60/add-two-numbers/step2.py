'''
headという変数名は答えのheadを表していそうだから、fake_headに変える
nowもtailに変える
whileが多いからまとめる。
    ただ、実際1つのループにまとめるのが困難なケースもある気がするので、そこは実装する前に考えたほうが良いかもしれない

口頭説明シミュレーション
    まず、fake_headを作ります。
    あとから後ろからノードをたどっていくのは大変なので、素早くheadを指せるポインタが欲しいからです。
    次に、現在処理しているノードを表すtailを用意します。
    また、l1とl2を足したときに繰り上がりが発生する可能性があるので、carryもここで用意しておきます。
    l1かl2がNoneでないか、carryが1の間ループをします。
    carryを入れる理由は、最後に繰り上がりだけ残った場合をループの中で処理したいからです。
    そしてsum_valという変数は、それらを足した値とします。
    carryを桁あふれ、つまりsum_valを10で割った商とします。
    また、sum_valの10で割ったあまりをtailの次のノードの値とします。
    そして、tail, l1, l2を次のステップへと進めます。
    こうすることで、問題を解くことができました。
    最後に桁上りしてl1とl2が終了する場合や、空のL1,l2を渡された場合にも対処できていることも確認できます。
    
    Firstly, we create "fake_head".
    This is because we want a pointer that can quickly point to the head.
    Next, we prepare "tail" that represents the node currently being processed.
    We also need to prepare "carry" because there is possibility of carry-over when l1 and l2 added.
    We loop while l1 or l2 is not None or if carry is 1.
    The reason for including "carry" is that we want to handle the case where only the carry remains in the loop.
    The variable "sum_val" is the value obtained by adding them together.
    Let carry be the overflow. In other words, it is the quotient of sum_val divided by 10.
    And let sum_val's remainder divided by 10 be the value of the next node of tail.
    Then we proceed to the next step for tail, l1, and l2.
    In this way, we have solved the problem.
    We can also confirm that we are able to deal with the case where l1 and l2 terminate after overflow or when an empty l1 and l2 are passed.
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
