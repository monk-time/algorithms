from typing import List


def count_happy(greed: List[int], cookie_sizes: List[int]):
    greed.sort()
    cookie_sizes.sort()
    i = 0
    for cookie in cookie_sizes:
        if cookie < greed[i]:
            continue
        i += 1
        if i == len(greed):
            break
    return i


if __name__ == '__main__':
    n = int(input())
    greed = list(map(int, input().split()))
    m = int(input())
    cookie_sizes = list(map(int, input().split()))
    print(count_happy(greed, cookie_sizes))
