from functools import reduce
from random import choice
from string import ascii_lowercase
from typing import Tuple

a = 1_000
m = 123_987_123


def polynomial_hash(s: str) -> int:
    return reduce(lambda acc, ch: (acc * a + ord(ch)) % m, s, 0)


def find_collision() -> Tuple[str, str]:
    strings = {}
    while True:
        s = ''.join(choice(ascii_lowercase) for _ in range(20))
        hash_val = polynomial_hash(s)
        if hash_val in strings and strings[hash_val] != s:
            return s, strings[hash_val]
        strings[hash_val] = s


if __name__ == '__main__':
    print(*find_collision(), sep='\n')
