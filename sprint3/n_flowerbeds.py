from collections.abc import Iterable


def union(segments: list[list[int]]) -> Iterable[list[int]]:
    segments.sort()
    left = 0
    while left < len(segments):
        segment_start, segment_end = segments[left]
        right = left + 1
        while right < len(segments) and segments[right][0] <= segment_end:
            segment_end = max(segment_end, segments[right][1])
            right += 1
        yield [segment_start, segment_end]
        left = right


if __name__ == '__main__':
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    for segment in union(segments):
        print(*segment)
