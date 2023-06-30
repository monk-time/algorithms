from math import ceil


def can_fit_at_x_distance(a: list[int], total_count: int, x: int) -> bool:
    count, last = 1, a[0]
    for value in a[1:]:
        if value - last < x:
            continue
        count += 1
        if count >= total_count:
            return True
        last = value
    return False


def max_min_distance(a: list[int], k: int) -> int:
    left, right = 1, a[-1] - a[0]
    while left <= right:
        if left == right:
            break
        mid = ceil((left + right) / 2)
        if can_fit_at_x_distance(a, k, mid):
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    n, k = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    print(max_min_distance(a, k))
