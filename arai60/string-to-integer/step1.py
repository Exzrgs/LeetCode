"""
25m

変数名や可読性に気を取られて時間がかかってしまった。
後半はそれを嫌がって少し雑になってしまった。
問題文を最後まで読んでおらず、オーバーフローが考慮できていなかった
空文字が与えられるなど、コーナーケースを考慮できていなかった
コードも改善点が多そうだし、取り組み方自体にも反省点が多い問題だった。
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        not_space_index = -1
        for i, c in enumerate(s):
            if c != " ":
                not_space_index = i-1
                break
        space_deleted_s = s[not_space_index+1:]

        if len(space_deleted_s) == 0:
            return 0

        sign = 1
        if space_deleted_s[0] == "+":
            sign_deleted_s = space_deleted_s[1:]
        elif space_deleted_s[0] == "-":
            sign = -1
            sign_deleted_s = space_deleted_s[1:]
        else:
            sign_deleted_s = space_deleted_s
        
        num_of_s = "0"
        index = 0
        while index < len(sign_deleted_s) and sign_deleted_s[index].isdecimal():
            num_of_s += sign_deleted_s[index]
            index += 1
        
        num = sign*int(num_of_s)
        max_num = 2**31 - 1
        min_num = -2**31
        if num > max_num:
            num = max_num
        if num < min_num:
            num = min_num

        return num
