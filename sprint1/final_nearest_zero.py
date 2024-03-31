"""ID посылки: 87592079."""

from math import inf


def nearest_zeroes(numbers: list[int]) -> list[int]:
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
    houses = [int(x) for x in input().split()]
    print(*nearest_zeroes(houses))
