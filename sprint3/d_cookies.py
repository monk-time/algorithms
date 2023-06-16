from typing import List


def count_happy(greed: List[int], cookies: List[int]):
    greed.sort()
    cookies.sort()
    i = 0
    for cookie in cookies:
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
    cookies = list(map(int, input().split()))
    print(count_happy(greed, cookies))
