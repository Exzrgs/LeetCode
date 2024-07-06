"""
https://github.com/kagetora0924/leetcode-grind/pull/11/files
    step3が王道
https://github.com/TORUS0818/leetcode/pull/11/files
    Counterやheapqなどいろいろな解き方が載っている

defaultdictのドキュメントを読む
    https://docs.python.org/ja/3.6/library/collections.html#collections.defaultdict
    dictのサブクラス
    コンストラクタの引数としてdefault_factoryを指定する。intとかlistとか
    
    d = {}
    for k, v in s:
        d.setdefault(k, []).append(v)
    とやってることは同じだが、速度はdefaultdictのほうが速い
ヒープについて
    https://medium.com/@yasufumy/data-structure-heap-ecfd0989e5be
    最小ヒープで考える
    二分木になっている
    親が子より必ず小さい
    heapify
        O(n)
        下からヒープ木を構成していく
        ヒープ木のノードに対して、木の高さだけ比較して交換する必要がある
        よって、O(ノードの数*その時の高さ)になり、
        1*logn + 2*log(n-1) + ...
        ~= logn^2 = 
    heappush
        O(logn)
        木の高さ分だけ更新する必要がある
    heappop
        O(logn)
        取り出すのはO(1)だが、ヒープを再構築するので、高さ分だけ更新
heapqのドキュメントを読む
    https://docs.python.org/ja/3/library/heapq.html
Counterのドキュメントを読む
"""

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1
        num_and_counts = []
        for n, count in num_to_count.items():
            num_and_counts.append((n, count))
        num_and_counts.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in num_and_counts][:k]

# count to numを作る
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1
        count_to_nums = [[] for _ in range(len(nums) + 1)]
        for n, count in num_to_count.items():
            count_to_nums[count].append(n)
        res = []
        for i in range(len(nums) - 1, 1, -1):
            for n in count_to_nums[i]:
                res.append(n)
                if len(res) == k:
                    return res

# heapqを使う
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        count_heap = []
        for n, count in count.items():
            heapq.heappush(count_heap, (count, n))
            if len(count_heap) > k:
                heapq.heappop(count_heap)
        return [n for _, n in count_heap]

# heapqの関数を使う
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        return [n for _, n in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

# Counter
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [n for n, _ in counter.most_common(k)]
