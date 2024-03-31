from functools import reduce
from itertools import combinations_with_replacement
from string import ascii_lowercase

a = 1_000
m = 123_987_123


def polynomial_hash(s: str) -> int:
    return reduce(lambda acc, ch: (acc * a + ord(ch)) % m, s, 0)


def find_collision() -> tuple[str, str]:
    strings, length = {}, 1
    while True:
        combs = combinations_with_replacement(ascii_lowercase, length)
        for s in map(''.join, combs):
            hash_val = polynomial_hash(s)
            if hash_val in strings:
                return s, strings[hash_val]
            strings[hash_val] = s
        length += 1


if __name__ == '__main__':
    print(*find_collision(), sep='\n')
