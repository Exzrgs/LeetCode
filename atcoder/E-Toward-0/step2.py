def parse_inputs():
    n, divider, divide_fee, dice_fee = map(int, input().split())
    return n, divider, divide_fee, dice_fee

def compute_expected_value(n, divider, divide_fee, dice_fee, memo):
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

def main():
    n, divider, divide_fee, dice_fee = parse_inputs()
    memo = dict()
    print(compute_expected_value(n, divider, divide_fee, dice_fee, memo))

if __name__ == '__main__':
    main()
