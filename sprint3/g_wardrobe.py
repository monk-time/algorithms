from collections import Counter
from typing import List


def count_colors(colors: List[int]) -> List[int]:
    counter = Counter(colors)
    for key in sorted(counter.keys()):
        for _ in range(counter[key]):
            yield key


if __name__ == '__main__':
    n = int(input())
    colors = list(map(int, input().split()))
    print(*count_colors(colors))
