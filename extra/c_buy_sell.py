def find_max_difference(a: list[int], money: int = 1000) -> tuple[int, int]:
    max_left, max_right, max_profit_coef = 0, 0, 1
    left = right = 0
    for i in range(1, len(a)):
        if a[i] < a[left]:
            left = i
        elif a[i] > a[left] and (right <= left or a[i] > a[right]):
            right = i
            profit_coef = a[right] / a[left]
            if a[left] <= money and profit_coef > max_profit_coef:
                max_left, max_right = left + 1, right + 1
                max_profit_coef = profit_coef
    return max_left, max_right


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(*find_max_difference(numbers), sep=' ')
