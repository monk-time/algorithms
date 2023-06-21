from typing import List


def has_repeats_at_dist(a: List[int], max_dist: int) -> bool:
    return False


if __name__ == '__main__':
    n, max_dist = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    print('YES' if has_repeats_at_dist(a, max_dist) else 'NO')
