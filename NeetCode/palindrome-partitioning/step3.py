# time: O(2^n * n) generating all possible substrings, check if it is palindrome
# space: O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palindromes = []
        
        def check_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def append_palindrome(index):
            if index == len(s):
                res.append(palindromes.copy())
                return
            
            for j in range(index, len(s)):
                if check_palindrome(s, index, j):
                    palindromes.append(s[index : j + 1])
                    append_palindrome(j + 1)
                    palindromes.pop()
        
        append_palindrome(0)
        return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palindromes = []
        
        def check_palindrome(s):
            if not s:
                return False
            
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def append_partitions(index, partition):
            if index == len(s):
                if not check_palindrome(partition):
                    return
                res.append(palindromes.copy() + [partition])
                return
            
            partition += s[index]
            append_partitions(index + 1, partition)
            
            if check_palindrome(partition):
                palindromes.append(partition)
                append_partitions(index + 1, "")
                palindromes.pop()
        
        append_partitions(0, "")
        return res
