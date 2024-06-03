"""
21m

考察：
    openかcloseかを入れる
    入ってるopenの数もカウントしておいて、それが正ならcloseも入れる
反省：
    できれば返り値を処理する形で書きたかったが、書き方がわからなかった
    popしなくてよいので、bfsでも楽に書けることまで考えればよかった。解き方を思いついても他の選択肢を軽く検討して、提示すべき
    解き方自体はすぐに思いついているのに、時間がかかるのをどうにかしたい。
        変数名を考えるのは少し慣れてきたが、全体でなぜここまで遅くなってしまっているのかは
        自分でもよくわかっていない。エディタを使用せずにすべて直打ちしているのも影響している？
        ただ、毎回ちゃんと反省をして演習量を積めば改善される気はしている。
        とりあえず変数名をすぐに思いつけるようにして、手戻りのないように実装できるようになろう。
"""

# dfs
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def append_bracket(bracket_limit, bracket_stack):
            if len(bracket_stack) == bracket_limit * 2:
                return bracket_stack
            
            open_count = bracket_stack.count("(")
            close_count = bracket_stack.count(")")
            if open_count < bracket_limit:
                new_bracket_stack = list(bracket_stack)
                new_bracket_stack.append("(")
                res = append_bracket(bracket_limit, new_bracket_stack)
                if res:
                    answer.append("".join(res))
            if open_count - close_count > 0:
                new_bracket_stack = list(bracket_stack)
                new_bracket_stack.append(")")
                res = append_bracket(bracket_limit, new_bracket_stack)
                if res:
                    answer.append("".join(res))
        
        append_bracket(n, [])
        return answer

# bfs
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bracket_combinations = []
        queue = deque()
        queue.append([])

        while len(queue) > 0:
            bracket_stack = queue.popleft()
            if len(bracket_stack) == 2 * n:
                bracket_combinations.append("".join(bracket_stack))
                continue
            
            open_count = bracket_stack.count("(")
            close_count = bracket_stack.count(")")
            if open_count < n:
                new_bracket_stack = list(bracket_stack)
                new_bracket_stack.append("(")
                queue.append(new_bracket_stack)
            if open_count - close_count > 0:
                new_bracket_stack = list(bracket_stack)
                new_bracket_stack.append(")")
                queue.append(new_bracket_stack)
        
        return bracket_combinations
