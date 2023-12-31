from collections import Counter
from itertools import pairwise


def min_to_delete(a: list[int]) -> int:
    counter = Counter(a)
    unique_nums = sorted(counter.keys())
    if len(unique_nums) < 2:
        return 0
    max_len = 1
    for x, y in pairwise(unique_nums):
        if abs(x - y) <= 1:
            max_len = max(counter[x] + counter[y], max_len)
    return len(a) - max_len


if __name__ == '__main__':
    n = int(input())
    a = [int(s) for s in input().split()]
    print(min_to_delete(a))
