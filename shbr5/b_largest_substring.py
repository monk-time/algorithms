from collections import defaultdict
from itertools import chain, pairwise


def find_max_good_substring_length(s: str, min_count: int) -> int:
    def rec(left: int, right: int):
        counter = defaultdict(list)
        for i in range(left, right + 1):
            counter[s[i]].append(i)
        bad_chars = (lst for lst in counter.values() if len(lst) < min_count)
        split_points = [left - 1, *sorted(chain(*bad_chars)), right + 1]
        if len(split_points) == 2:
            return right - left + 1
        return max(rec(a + 1, b - 1) for a, b in pairwise(split_points))

    return rec(0, len(s) - 1)


if __name__ == '__main__':
    n, min_count = (int(s) for s in input().split())
    s = input()
    print(find_max_good_substring_length(s, min_count))
