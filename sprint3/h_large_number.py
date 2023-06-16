from functools import cmp_to_key
from typing import List


def compare(a: str, b: str) -> int:
    return -1 if a + b < b + a else 1 if a + b > b + a else 0


def largest_number(numbers: List[str]) -> str:
    return ''.join(sorted(numbers, key=cmp_to_key(compare), reverse=True))


if __name__ == '__main__':
    _ = int(input())
    numbers = input().split()
    print(largest_number(numbers))
