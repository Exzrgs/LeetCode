"""
we are gonna append value to the stack
when we find the operator, we pop 2 values from stack and operate them, then push the result to the stack again
"""

from operator import add, sub, mul, truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        elements = []
        operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': truediv,
        }
        for token in tokens:
            if token in operators:
                b, a = elements.pop(), elements.pop()
                elements.append(int(operators[token](a, b)))
            else:
                elements.append(int(token))
        return elements[0]

# ちゃんと場合分けする
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        elements = []
        for token in tokens:
            if token == '+':
                elements.append(elements.pop() + elements.pop())
            elif token == '-':
                b, a = elements.pop(), elements.pop()
                elements.append(a - b)
            elif token == '*':
                elements.append(elements.pop() * elements.pop())
            elif token == '/':
                b, a = elements.pop(), elements.pop()
                elements.append(int(a / b))
            else:
                elements.append(int(token))
        return elements[0]
