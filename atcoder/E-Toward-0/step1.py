"""
再帰関数で求める
f(n) = (f(n) + f(n // 2) + f(n // 3)...) / 6 + dice_fee
→ 5/6*f(n) = (f(n // 2) + f(n // 3)...) / 6 + dice_fee
→ f(n) = (f(n // 2) + f(n // 3)...) / 5 + 6/5*dice_fee
"""

n, divider, divide_fee, dice_fee = map(int, input().split())
memo = dict()
def compute_expected_value(n):
    if n == 0:
        return 0
    if n not in memo:
        divide_expected_value = compute_expected_value(n // divider) + divide_fee
        dice_expected_value = 6 * dice_fee
        for i in range(2, 7):
            dice_expected_value += compute_expected_value(n // i)
        dice_expected_value /= 5
        memo[n] = min(divide_expected_value, dice_expected_value)
    return memo[n]
print(compute_expected_value(n))
