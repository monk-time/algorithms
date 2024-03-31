def factorization(n: int):
    if n <= 1:
        yield 1
        return
    factor = 2
    while factor**2 <= n:
        if n % factor == 0:
            yield factor
            n //= factor
        else:
            factor += 1
    if n > 1:
        yield n


if __name__ == '__main__':
    n = int(input())
    print(' '.join(map(str, factorization(n))))
