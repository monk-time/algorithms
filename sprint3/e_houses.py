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


if __name__ == '__main__':
    _, budget = map(int, input().split())
    houses = list(map(int, input().split()))
    print(count_houses(houses, budget))
