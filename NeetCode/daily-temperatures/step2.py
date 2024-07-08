"""
d2 → before_day
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = [0] * len(temperatures)
        stack = []
        for d, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                before_day = stack.pop()[0]
                wait_days[before_day] = d - before_day
            stack.append((d, t))
        return wait_days
