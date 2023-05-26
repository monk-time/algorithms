from typing import List


def union(segments: List[List[int]]) -> List[List[int]]:
    segments.sort()
    i = 0
    while i < len(segments):
        a, b = segments[i]
        j = i + 1
        while j < len(segments) and segments[j][0] <= b:
            b = max(b, segments[j][1])
            j += 1
        yield [a, b]
        i = j


if __name__ == '__main__':
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    for segment in union(segments):
        print(*segment)
