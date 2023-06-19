from typing import List


def unique(a: List) -> List:
    return list({key: None for key in a}.keys())


if __name__ == '__main__':
    count = int(input())
    a = [input() for _ in range(count)]
    print(*unique(a), sep='\n')
