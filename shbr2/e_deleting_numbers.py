from typing import List


def min_to_delete(a: List[int]) -> int:
    return 1


if __name__ == '__main__':
    n = int(input())
    a = [int(s) for s in input().split()]
    print(min_to_delete(a))
