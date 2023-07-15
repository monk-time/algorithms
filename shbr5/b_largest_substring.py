from collections import defaultdict
from itertools import chain, pairwise


def find_max_good_substring_length(s: str, min_count: int) -> int:
    def rec(left: int, right: int):
        counter = defaultdict(list)
        for i in range(left, right + 1):
            counter[s[i]].append(i)
        split_points = sorted(
            chain.from_iterable(
                lst for lst in counter.values() if len(lst) < min_count
            )
        )
        if not split_points:
            return right - left + 1
        split_points = [left - 1, *split_points, right + 1]
        return max(rec(a + 1, b - 1) for a, b in pairwise(split_points))

    return rec(0, len(s) - 1)


if __name__ == '__main__':
    n, min_count = [int(s) for s in input().split()]
    s = input()
    print(find_max_good_substring_length(s, min_count))
