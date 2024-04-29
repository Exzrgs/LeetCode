"""
5m
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_NUM = 2**31 - 1
        MIN_NUM = -(2 ** 31)

        index = 0
        while index < len(s) and s[index] == ' ':
            index += 1
        if index == len(s):
            return 0
        
        sign = 1
        if s[index] == '+':
            index += 1
        elif s[index] == '-':
            sign = -1
            index += 1
        
        abs_num = 0
        while index < len(s) and '0' <= s[index] <= '9':
            abs_num = abs_num*10 + int(s[index])
            index += 1
        num = sign * abs_num

        if num > MAX_NUM:
            num = MAX_NUM
        elif num < MIN_NUM:
            num = MIN_NUM
        
        return num
