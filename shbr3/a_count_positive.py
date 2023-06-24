from itertools import accumulate
from typing import Iterable


def count_positive(a: list[int], queries: list[list[int]]) -> Iterable[int]:
    start_counts = list(accumulate(a, lambda acc, x: acc + (x > 0), initial=0))
    for left, right in queries:
        yield start_counts[right] - start_counts[left - 1]


def main():
    _ = int(input())
    a = [int(s) for s in input().split()]
    query_count = int(input())
    queries = [[int(s) for s in input().split()] for _ in range(query_count)]
    print(*count_positive(a, queries), sep='\n')


if __name__ == '__main__':
    main()
