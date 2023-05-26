from typing import List


def binary_search(a: List[int], k: int, left: int, right: int) -> int:
    while left < right - 1:
        mid = (left + right) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            right = mid
        else:
            left = mid
    return left if a[left] == k else -1


DAY_OFFSET = 1


def left_binary_search_mod(a: List[int], k: int, left: int, right: int) -> int:
    while left < right - 1:
        mid = (left + right) // 2
        if a[mid] >= k:
            if a[mid - 1] < k:
                return mid + DAY_OFFSET
            right = mid
        else:
            left = mid
    return left + DAY_OFFSET if a[left] >= k else -1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cost = int(input())
    print(
        left_binary_search_mod(a, cost, 0, len(a)),
        left_binary_search_mod(a, 2 * cost, 0, len(a)),
    )
