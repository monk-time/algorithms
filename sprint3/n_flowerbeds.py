from typing import Iterable, List


def union(segments: List[List[int]]) -> Iterable[List[int]]:
    segments.sort()
    i = 0
    while i < len(segments):
        left, right = segments[i]
        j = i + 1
        while j < len(segments) and segments[j][0] <= right:
            right = max(right, segments[j][1])
            j += 1
        yield [left, right]
        i = j


if __name__ == '__main__':
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    for segment in union(segments):
        print(*segment)
