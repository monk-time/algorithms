"""ID посылки: 87592136."""

from collections import Counter
from itertools import chain
from typing import List


def max_score(field: List[str], k: int) -> int:
    counter = Counter(chain(*field))
    counter.pop('.', None)
    return sum(k * 2 >= value for value in counter.values())


if __name__ == '__main__':
    k = int(input())
    field = [input() for _ in range(4)]
    print(max_score(field, k))
