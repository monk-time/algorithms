from functools import cache


@cache
def fib(n: int) -> int:
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
