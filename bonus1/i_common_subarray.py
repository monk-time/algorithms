from functools import reduce
from typing import List


def polynomial_hash(a: List[int]) -> int:
    m = 10**9 + 7
    q = 257
    return reduce(lambda acc, x: (acc * q + x + 1) % m, a, 0)


def longest_common_subarray_len(a: List[int], b: List[int]) -> int:
    m = 10**9 + 7
    q = 257
    if len(a) > len(b):
        a, b = b, a

    max_len = 0
    hashes_a = [x + 1 for x in a]
    hashes_a_dict = {h: i for i, h in enumerate(hashes_a)}
    for x in b:
        if (x + 1) in hashes_a_dict:
            max_len = 1
            break
    else:  # no break
        return 0

    pr, h = [], 0
    for x in b:
        h = (h * q + x + 1) % m
        pr.append(h)
    pows = [pow(q, n, m) for n in range(len(b))]

    len_a, len_b = len(a), len(b)
    for n in range(2, len_a + 1):
        next_hashes_a = []
        for i, h in enumerate(hashes_a):
            if i == len_a - n + 1:
                continue
            h = (h * q + (a[i + n - 1] + 1)) % m
            # assert h == polynomial_hash(a[i : i + n])
            next_hashes_a.append(h)
            hashes_a_dict[h] = i
        hashes_a = next_hashes_a

        for i in range(len_b - n + 1):
            j = i + n - 1
            h = (pr[j] - pows[j - i + 1] * pr[i - 1]) % m if i > 0 else pr[j]
            # assert h == polynomial_hash(b[i : i + n])
            if h in hashes_a_dict:
                max_len = n
                break
        else:  # no break
            return max_len

    return max_len


if __name__ == '__main__':
    # n = int(input())
    # a = [int(s) for s in input().split()]
    # m = int(input())
    # b = [int(s) for s in input().split()]
    # print(longest_common_subarray_len(a, b))

    # print(f'a: len={len(a)}, unique={len(set(a))}, min={min(a)}, max={max(a)}')
    # print(f'b: len={len(b)}, unique={len(set(b))}, min={min(b)}, max={max(b)}')

    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # b = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # print(longest_common_subarray_len(a, b))

    from time import time

    now = time()
    a = [1] * 10_000
    b = [1] * 5_000 + [2] * 5_000

    print(longest_common_subarray_len(a, b))
    print(f'{time() - now:.3f} sec')

    # import cProfile

    # with cProfile.Profile() as pr:
    #     print(longest_common_subarray_len(a, b))
    # pr.print_stats()
