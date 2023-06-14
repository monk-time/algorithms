import time
from itertools import chain, repeat


def find_max_difference(a: list[int]) -> tuple[int, int]:
    max_left, max_right, max_profit_coef = 0, 0, 1
    left = right = 0
    for i in range(1, len(a)):
        if a[i] < a[left]:
            left = i
        elif a[i] > a[left] and (right <= left or a[i] > a[right]):
            right = i
            profit_coef = a[right] / a[left]
            if profit_coef > max_profit_coef:
                max_left, max_right = left + 1, right + 1
                max_profit_coef = profit_coef
    return max_left, max_right


def find_max_difference_bad(
    a: list[int], money: int = 1000
) -> tuple[int, int]:
    size = len(a)
    max_left, max_right, max_diff = 0, 0, 0

    if len(a) > 1:
        left = 0
        while left < size - 1:
            while a[left] >= a[left + 1] and left < size - 2:
                left += 1

            if left < size - 2:
                right = max(range(left + 1, size), key=lambda x: (a[x], x))
                left = min(range(left, right), key=lambda x: (a[x], x))
                diff = (money // a[left]) * (a[right] - a[left])
                if diff > max_diff:
                    max_diff = diff
                    max_left, max_right = left, right
            else:
                break

            left = right

    if max_diff:
        max_left += 1
        max_right += 1
    return max_left, max_right


if __name__ == '__main__':
    size = 100_000
    max_val = 5_000
    mid = max_val // 2
    numbers = list(
        chain.from_iterable(
            zip(range(1, mid + 1), reversed(range(mid + 1, max_val + 1)))
        )
    )
    numbers = list(
        chain.from_iterable(repeat(x, size // max_val) for x in numbers)
    )

    now = time.time()
    print(find_max_difference_bad(numbers))
    diff = time.time() - now
    print(diff)

    n = int(input())
    numbers = list(map(int, input().split()))
    print(*find_max_difference(numbers), sep=' ')
