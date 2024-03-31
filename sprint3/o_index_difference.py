from bisect import bisect


def count_pairs(a: list[int], max_diff: int) -> int:
    """Count pairs with absolute difference less than or equal to max_diff.

    For every element count the number of such pairs in a[i:].
    Bisect returns position of the first element higher than
    a[i] + max_diff, which is also the number of elements
    less than or equal to a[i] + max_diff.
    (i + 1) is the number of elements from start to i.
    """
    return sum(bisect(a, n + max_diff) - (i + 1) for i, n in enumerate(a))


def min_diff_by_index(a: list[int], index: int):
    a = sorted(a)
    min_diff = min(a[i + 1] - a[i] for i in range(len(a) - 1))
    max_diff = a[-1] - a[0]

    while min_diff < max_diff:
        mid = (min_diff + max_diff) // 2
        if count_pairs(a, mid) < index:
            min_diff = mid + 1
        else:
            max_diff = mid

    return min_diff


if __name__ == '__main__':
    _ = int(input())
    nums = list(map(int, input().split()))
    index = int(input())
    print(min_diff_by_index(nums, index))
