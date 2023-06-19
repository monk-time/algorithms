from itertools import chain, product
from math import sqrt
from typing import List, Tuple


Coord = Tuple[int, int]
Coords = List[Coord]


def get_segment(c: Coord) -> Coord:
    return (c[0] // 10, c[1] // 10)


def is_near(c1: Coord, c2: Coord) -> bool:
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) <= 20


def subway_with_most_stops(subways: Coords, stops: Coords) -> int:
    stops_by_segment = {}
    for stop in stops:
        segment = get_segment(stop)
        if segment in stops_by_segment:
            stops_by_segment[segment].append(stop)
        else:
            stops_by_segment[segment] = [stop]
    max_count, max_subway_index = 0, 0
    for index, subway in enumerate(subways):
        seg_x, seg_y = get_segment(subway)
        # Segments covers 50x50 area around subway segment (25 segments)
        # plus a lower right corner strip of 11 segments for the most
        # distant stops.
        area = chain.from_iterable(
            stops_by_segment.get((seg_x + dx, seg_y + dy), [])
            for dx, dy in product(range(-2, 4), repeat=2)
        )
        count = sum(is_near(subway, stop) for stop in area)
        if count > max_count:
            max_count = count
            max_subway_index = index
    return max_subway_index + 1


def main():
    n = int(input())
    subways = [tuple(int(s) for s in input().split()) for _ in range(n)]
    m = int(input())
    stops = [tuple(int(s) for s in input().split()) for _ in range(m)]
    print(subway_with_most_stops(subways, stops))


if __name__ == '__main__':
    main()
