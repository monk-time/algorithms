def fib_mod(n: int, k: int) -> int:
    prev = last = 1
    divisor = 10 ** k
    for _ in range(n - 1):
        prev, last = last, (prev + last) % divisor
    return last


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(fib_mod(n, k))
