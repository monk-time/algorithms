from bisect import bisect_left
from typing import List


def binary_search(a: List[int], k: int, left: int, right: int) -> int:
    while left < right:
        mid = (left + right) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            right = mid
        else:
            left = mid
    return -1


DAY_OFFSET = 1


def left_binary_search_mod(a: List[int], k: int) -> int:
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] >= k:
            if mid == 0 or a[mid - 1] < k:
                return mid + DAY_OFFSET
            right = mid
        else:
            left = mid if left < mid else right
    return -1


def bisect(a: List[int], k: int) -> int:
    pos = bisect_left(a, k)
    return pos + DAY_OFFSET if pos < len(a) else -1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cost = int(input())
    print(
        left_binary_search_mod(a, cost),
        left_binary_search_mod(a, 2 * cost),
    )
