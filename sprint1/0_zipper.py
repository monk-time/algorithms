from itertools import chain


def zipper(a: list[int], b: list[int]) -> list[int]:
    return list(chain(*zip(a, b)))


def read_input() -> tuple[list[int], list[int]]:
    _ = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


if __name__ == '__main__':
    a, b = read_input()
    print(' '.join(map(str, zipper(a, b))))
