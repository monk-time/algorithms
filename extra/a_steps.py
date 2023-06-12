def steps(x: int) -> int:
    n, total = 0, 0
    while total <= x:
        n += 1
        total += n
    return n - 1


if __name__ == '__main__':
    n = int(input())
    print(steps(n))
