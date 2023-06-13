import math


def steps_iter(x: int) -> int:
    n, total = 0, 0
    while total <= x:
        n += 1
        total += n
    return n - 1


def steps(x: int) -> int:
    return math.floor((math.sqrt(8 * x + 1) - 1) / 2)


if __name__ == '__main__':
    n = int(input())
    print(steps(n))
