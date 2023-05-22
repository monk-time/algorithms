def check_parity(a: int, b: int, c: int) -> str:
    same_parity = a % 2 == b % 2 == c % 2
    return ('FAIL', 'WIN')[same_parity]


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(check_parity(a, b, c))
