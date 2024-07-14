"""
Question:
    How is the length of nums1 and nums2?
        (Can nums1 and nums2 be empty array?)
    What is the constraint of nums element? max and min
Discussion:
    We can find the median by using binary search
    left: -10^6
    right: 10^6
    We are gonna compute (nums1 index + nums2 index)
    and the index is found by binary search
    time complexity: O(log(n + m)^2)
    space complexity: O(1)
Simple Test:
    nums1: [1, 3]
    nums2: [2, 4]

    nums1: [1]
    nums2: [1, 2]

もっと計算量が悪いがシンプルな方法から始めてよいかも
実際解けなくても、いろいろな解き方を検討できていることを見せる
あと、練習だからもっといろいろな解き方を実際書いてみてもよい。
もう少しleetcodeのsolutionを漁る

https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/4070500/99-journey-from-brute-force-to-most-optimized-three-approaches-easy-to-understand/

二分探索解法
nums1において、中央値の境界になる場所を探す。
つまり、nums1_leftが境界の左、nums1_rightが境界の右
(nums1_left, nums2_left)(nums1_right, nums2_right)
という形を作りたい。nums1とnums2の順番はどちらでもよい
"""

# merge
# time: O(n + m)
# space: O(n + m)
class Solution:
    def merge_sorted_array(self, nums1, nums2):
        merged_nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1
        while i < len(nums1):
            merged_nums.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged_nums.append(nums2[j])
            j += 1
        return merged_nums

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = self.merge_sorted_array(nums1, nums2)
        median = (merged_nums[(len(merged_nums) - 1) // 2] + merged_nums[len(merged_nums) // 2]) / 2
        return median

# two pointer
# time: O(n + m)
# space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        m1 = 0
        m2 = 0
        while i + j <= (len(nums1) + len(nums2)) // 2:
            m2 = m1
            if i == len(nums1):
                m1 = nums2[j]
                j += 1
            elif j == len(nums2):
                m1 = nums1[i]
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (m1 + m2) / 2
        else:
            return float(m1)

# O(log(n + m))
# (むずかしい...)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half_length = (len(nums1) + len(nums2)) // 2
        # we want to make (half_length - mid) positive value
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1) - 1
        while True:
            index1 = (left + right) // 2
            index2 = half_length - index1 - 2

            nums1_left = nums1[index1] if index1 >= 0 else float('-inf')
            nums1_right = nums1[index1 + 1] if index1 + 1 < len(nums1) else float('inf')
            nums2_left = nums2[index2] if index2 >= 0 else float('-inf')
            nums2_right = nums2[index2 + 1] if index2 + 1 < len(nums2) else float('inf')
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                total_length = (len(nums1) + len(nums2))
                if total_length % 2 == 1:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = index1 - 1
            else:
                left = index1 + 1

