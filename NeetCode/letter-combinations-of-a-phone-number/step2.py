class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        combs = []
        
        def dfs(index):
            if index == len(digits):
                res.append("".join(combs))
                return
            
            for c in digits_to_letters[digits[index]]:
                combs.append(c)
                dfs(index + 1)
                combs.pop()
        
        if digits:
            dfs(0)
        return res
