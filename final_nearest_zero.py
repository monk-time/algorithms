"""ID посылки: 87586734."""

from math import inf
from typing import List


def parse_list(s: str) -> List[int]:
    return [int(x) for x in s.split()]


def list_to_str(a: List[int]) -> str:
    return ' '.join(map(str, a))


def nearest_zeroes(numbers: List[int]) -> List[int]:
    distances = []
    last_zero = -1
    for i, value in enumerate(numbers):
        if value:
            distances.append(i - last_zero if last_zero != -1 else inf)
            continue
        for j in range(last_zero + 1, i):
            distances[j] = min(distances[j], i - j)
        distances.append(0)
        last_zero = i
    return distances


if __name__ == '__main__':
    n = int(input())
    houses = parse_list(input())
    print(list_to_str(nearest_zeroes(houses)))
