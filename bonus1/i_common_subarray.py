from typing import List


def has_common_subarray_of_len(a: List[int], b: List[int], n: int) -> bool:
    m1, m2 = 10**9 + 7, 10**9 + 9
    q1, q2 = 31, 29
    q1_big, q2_big = pow(q1, n - 1, m1), pow(q2, n - 1, m2)

    hashes_a_dict = {}
    h1, h2 = 0, 0
    for i in range(n):
        h1 = (h1 * q1 + a[i] + 1) % m1
        h2 = (h2 * q2 + a[i] + 1) % m2
    hashes_a_dict[(h1, h2)] = 0
    for i in range(1, len(a) - n + 1):
        h1 = ((h1 - (a[i - 1] + 1) * q1_big) * q1 + a[i + n - 1] + 1) % m1
        h2 = ((h2 - (a[i - 1] + 1) * q2_big) * q2 + a[i + n - 1] + 1) % m2
        hashes_a_dict[(h1, h2)] = i

    h1, h2 = 0, 0
    for i in range(n):
        h1 = (h1 * q1 + b[i] + 1) % m1
        h2 = (h2 * q2 + b[i] + 1) % m2
    if (h1, h2) in hashes_a_dict:
        return True
    for i in range(1, len(b) - n + 1):
        h1 = ((h1 - (b[i - 1] + 1) * q1_big) * q1 + b[i + n - 1] + 1) % m1
        h2 = ((h2 - (b[i - 1] + 1) * q2_big) * q2 + b[i + n - 1] + 1) % m2
        if (h1, h2) in hashes_a_dict:
            return True

    return False


def longest_common_subarray_len(a: List[int], b: List[int]) -> int:
    if len(a) > len(b):
        a, b = b, a

    max_len = 0
    left, right = 1, len(a)
    while left <= right:
        mid = (left + right) // 2
        if has_common_subarray_of_len(a, b, mid):
            max_len = mid
            left = mid + 1
        else:
            right = mid - 1
    return max_len


if __name__ == '__main__':
    n = int(input())
    a = [int(s) for s in input().split()]
    m = int(input())
    b = [int(s) for s in input().split()]
    print(longest_common_subarray_len(a, b))
