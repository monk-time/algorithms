from collections import Counter


def majority(a: list[int]) -> int:
    return Counter(a).most_common(1)[0][0]


if __name__ == '__main__':
    n = int(input())
    a = [int(s) for s in input().split()]
    print(majority(a))
