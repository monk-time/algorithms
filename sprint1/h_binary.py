from itertools import zip_longest


def binary_sum(a: str, b: str) -> str:
    result, carry_over = '', 0
    for m, n in zip_longest(a[::-1], b[::-1], fillvalue='0'):
        carry_over, digit = divmod(int(m) + int(n) + carry_over, 2)
        result += str(digit)
    return '1' * carry_over + result[::-1]


if __name__ == '__main__':
    print(binary_sum(input(), input()))
