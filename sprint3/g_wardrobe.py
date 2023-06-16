from collections import Counter
from typing import List


def counting_sort(a: List[int]) -> List[int]:
    for key, count in sorted(Counter(a).items()):
        for _ in range(count):
            yield key


if __name__ == '__main__':
    _ = int(input())
    a = list(map(int, input().split()))
    print(*counting_sort(a))
