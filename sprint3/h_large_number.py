from typing import List


def largest_number(numbers: List[str]) -> str:
    return ''.join(sorted(numbers, reverse=True))


if __name__ == '__main__':
    n = int(input())
    numbers = input().split()
    print(largest_number(numbers))
