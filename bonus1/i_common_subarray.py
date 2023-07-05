from collections import defaultdict
from functools import reduce
from typing import List, DefaultDict


m, q = 10**9 + 7, 257


def prefix_hash(a: List[int], n: int) -> int:
    return reduce(lambda acc, i: (acc * q + a[i] + 1) % m, range(n), 0)


def is_not_collision(
    a: List[int], b: List[int], n: int, a_indices: List[int], b_index: int
) -> bool:
    return any(
        all(a[a_index + i] == b[b_index + i] for i in range(n))
        for a_index in a_indices
    )


def has_common_subarray_of_len(a: List[int], b: List[int], n: int) -> bool:
    q_big = pow(q, n - 1, m)

    a_hashes: DefaultDict[int, list[int]] = defaultdict(list)
    h = prefix_hash(a, n)
    a_hashes[h].append(0)
    for i in range(1, len(a) - n + 1):
        h = ((h - (a[i - 1] + 1) * q_big) * q + a[i + n - 1] + 1) % m
        a_hashes[h].append(i)

    h = prefix_hash(b, n)
    if h in a_hashes and is_not_collision(a, b, n, a_hashes[h], 0):
        return True
    for i in range(1, len(b) - n + 1):
        h = ((h - (b[i - 1] + 1) * q_big) * q + b[i + n - 1] + 1) % m
        if h in a_hashes and is_not_collision(a, b, n, a_hashes[h], i):
            return True

    return False


def longest_common_subarray_len(a: List[int], b: List[int]) -> int:
    if len(a) > len(b):
        a, b = b, a

    left, right = 0, len(a)
    while left < right:
        mid = (left + right + 1) // 2
        if has_common_subarray_of_len(a, b, mid):
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    n = int(input())
    a = [int(s) for s in input().split()]
    m = int(input())
    b = [int(s) for s in input().split()]
    print(longest_common_subarray_len(a, b))
