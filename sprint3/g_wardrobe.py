from collections import Counter
from collections.abc import Iterable


def counting_sort(a: list[int]) -> Iterable[int]:
    for key, count in sorted(Counter(a).items()):
        for _ in range(count):
            yield key


if __name__ == '__main__':
    _ = int(input())
    a = list(map(int, input().split()))
    print(*counting_sort(a))
