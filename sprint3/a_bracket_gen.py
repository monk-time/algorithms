def bracket_gen(n: int, left: int = 0, right: int = 0, s: str = ''):
    if left == right == n:
        yield s
    if left < n:
        yield from bracket_gen(n, left + 1, right, f'{s}(')
    if right < left:
        yield from bracket_gen(n, left, right + 1, f'{s})')


if __name__ == '__main__':
    n = int(input())
    for s in bracket_gen(n):
        print(s)
