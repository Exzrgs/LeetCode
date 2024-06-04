"""
文字列の長さは重要
    100
    これだと、順列を求めてとかはキビシイ
要は、出現回数が同じなら良い
もしくは、ソートした結果が同じでもよい
    これがよさそう

5m

sorted(s)で返るのはlistじゃないことに注意
.values()で返るのもlistじゃなくてdict_valuesという定義されたオブジェクト?
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_strs = defaultdict(list)
        for s in strs:
            sorted_str_to_strs["".join(sorted(s))].append(s)
        return sorted_str_to_strs.values()
