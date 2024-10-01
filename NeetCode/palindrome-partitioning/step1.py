class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partitions = []
        
        def check_palindrome(s):
            if not s:
                return False
            
            front = 0
            back = len(s) - 1
            while front <= back and s[front] == s[back]:
                front += 1
                back -= 1
            return front > back
        
        def append_palindrome(index, partition):
            if index == len(s):
                if not check_palindrome(partition):
                    return
                res.append(partitions.copy() + [partition])
                return
            
            append_palindrome(index + 1, partition + s[index])
            
            if check_palindrome(partition):
                partitions.append(partition)
                append_palindrome(index + 1, s[index])
                partitions.pop()
        
        append_palindrome(0, "")
        return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partitions = []
        
        def check_palindrome(s):
            if not s:
                return False
            
            front = 0
            back = len(s) - 1
            while front <= back and s[front] == s[back]:
                front += 1
                back -= 1
            return front > back
        
        def append_palindrome(index, partition):
            if index == len(s):
                if not check_palindrome(partition):
                    return
                res.append(partitions.copy() + [partition])
                return
            
            append_palindrome(index + 1, partition + s[index])
            
            if check_palindrome(partition):
                partitions.append(partition)
                append_palindrome(index + 1, s[index])
                partitions.pop()
        
        append_palindrome(0, "")
        return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partitions = []
        
        def check_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def append_palindromes(index):
            if index == len(s):
                res.append(partitions.copy())
                return
            
            for j in range(index, len(s)):
                if check_palindrome(s, index, j):
                    partitions.append(s[index : j + 1])
                    append_palindromes(j + 1)
                    partitions.pop()
        
        append_palindromes(0)
        return res
