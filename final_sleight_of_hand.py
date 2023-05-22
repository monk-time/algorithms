from collections import Counter
from itertools import chain


def max_score(field: list[str], k: int) -> int:
    counter = Counter(chain(*field))
    counter.pop('.')
    return sum(k * 2 >= value for value in counter.values())


if __name__ == '__main__':
    k = int(input())
    field = [input() for _ in range(4)]
    print(max_score(field, k))
