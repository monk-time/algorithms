from itertools import accumulate
from operator import add

MAX_VALUE = 10_000


def thickness(socks: list[list[int]], points: list[int]) -> list[int]:
    counter = [0] * (MAX_VALUE + 1)
    for start, end in socks:
        counter[start - 1] += 1
        counter[end] -= 1
    counter = list(accumulate(counter, add))
    return [counter[p - 1] for p in points]


if __name__ == '__main__':
    max_value, sock_count, point_count = [int(s) for s in input().split()]
    socks = [[int(s) for s in input().split()] for _ in range(sock_count)]
    points = [int(input()) for _ in range(point_count)]
    print(*thickness(socks, points), sep='\n')
