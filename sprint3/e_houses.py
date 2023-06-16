from itertools import accumulate
from typing import List


def count_houses(houses: List[int], budget: int) -> int:
    houses.sort()
    total = count = 0
    for house in houses:
        total += house
        if total > budget:
            break
        count += 1
    return count


def count_houses_acc(houses: List[int], budget: int) -> int:
    sums = accumulate(sorted(houses))
    return next((i for i, acc in enumerate(sums) if acc > budget), len(houses))


if __name__ == '__main__':
    _, budget = map(int, input().split())
    houses = list(map(int, input().split()))
    print(count_houses(houses, budget))
