from array import array
from functools import reduce
from random import choice
from string import ascii_lowercase
import time
from typing import List

from psutil import Process


def polynomial_hash(a: int, m: int, s: str) -> int:
    return reduce(lambda acc, ch: (acc * a + ord(ch)) % m, s, 0)


def window_hashes(a: int, m: int, s: str, size: int) -> List[int]:
    b = pow(a, size - 1, m)
    h = polynomial_hash(a, m, s[:size])
    hashes = array('l')
    hashes.append(h)
    for i in range(len(s) - size):
        h = ((h - ord(s[i]) * b) * a + ord(s[i + size])) % m
        hashes.append(h)
    return hashes


def all_window_hashes(a: int, m: int, s: str) -> List[List[int]]:
    return [window_hashes(a, m, s, size) for size in range(1, len(s) + 1)]


def main():
    a = int(input())
    m = int(input())
    s = input()
    count = int(input())
    hashes = all_window_hashes(a, m, s)
    for _ in range(count):
        i, j = (int(s) for s in input().split())
        print(hashes[j - i][i - 1])


if __name__ == '__main__':
    # main()
    now = time.time()
    s = ''.join(choice(ascii_lowercase) for _ in range(3_000))
    hashes = all_window_hashes(1000, 10_000_000, s)
    print(f'{time.time() - now} sec')
    max_memory = round(Process().memory_info().peak_wset / 1024 / 1024)
    print(f'{max_memory} MB')
