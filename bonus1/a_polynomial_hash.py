from functools import reduce


def polynomial_hash(a: int, m: int, s: str) -> int:
    return reduce(lambda acc, ch: (acc * a + ord(ch)) % m, s, 0)


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()
    print(polynomial_hash(a, m, s))
