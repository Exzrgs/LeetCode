"""
https://leetcode.com/problems/group-anagrams/solutions/3687735/beats-100-c-java-python-beginner-friendly/?envType=problem-list-v2&envId=me1nua2e
-> anagram_map なるほど
https://github.com/SuperHotDogCat/coding-interview/pull/13/files
-> sorted_str_to_anagramsのほうがよさそうだな
https://github.com/t-ooka/leetcode/pull/2/files
-> 出現回数を持つやり方。26個のタプルを入れるのに、listからtupleに変換すればよいのはたしかに

sorted_str_to_strs.values() -> list(sorted_str_to_strs.values())
sorted_str_to_strs -> sorted_str_to_anagrams
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_anagrams = defaultdict(list)
        for s in strs:
            sorted_str_to_anagrams["".join(sorted(s))].append(s)
        return list(sorted_str_to_anagrams.values())

# 出現回数を持つ
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        NUM_ALPHABET = 26
        sorted_str_to_anagrams = defaultdict(list)
        for s in strs:
            char_count = [0] * NUM_ALPHABET
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            sorted_str_to_anagrams[tuple(char_count)].append(s)
        return list(sorted_str_to_anagrams.values())
