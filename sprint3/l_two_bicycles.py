from bisect import bisect_left
from typing import List


def binary_search(a: List[int], k: int) -> int:
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            right = mid
        else:
            left = mid + 1
    return -1


DAY_OFFSET = 1


def left_binary_search(a: List[int], k: int) -> int:
    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] >= k:
            right = mid
        else:
            left = mid + 1
    return left + DAY_OFFSET if a and a[left] >= k else -1


def left_binary_search_rec(a: List[int], k: int) -> int:
    def rec(left: int, right: int):
        if left > right:
            return -1
        mid = (left + right) // 2
        if a[mid] >= k:
            if left == mid:
                return mid + DAY_OFFSET
            return rec(left, mid)
        return rec(mid + 1, right)

    return rec(0, len(a) - 1)


def bisect(a: List[int], k: int) -> int:
    pos = bisect_left(a, k)
    return pos + DAY_OFFSET if pos < len(a) else -1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cost = int(input())
    print(
        left_binary_search(a, cost),
        left_binary_search(a, 2 * cost),
    )
