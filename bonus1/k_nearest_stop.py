from collections import Counter
from itertools import product

Coord = tuple[int, int]
Coords = list[Coord]


def get_segment(c: Coord) -> Coord:
    return (c[0] // 5, c[1] // 5)


def subway_with_most_stops(subways: Coords, stops: Coords) -> int:
    stops_by_segment = {}
    for stop in stops:
        segment = get_segment(stop)
        if segment in stops_by_segment:
            stops_by_segment[segment][stop] += 1
        else:
            stops_by_segment[segment] = Counter([stop])
    max_count, max_subway_index = 0, 0
    for index, subway in enumerate(subways):
        seg_x, seg_y = get_segment(subway)
        count = 0
        # Check 81 segments in 50x50 area around the subway segment
        for dx, dy in product(range(-4, 5), repeat=2):
            segment = (seg_x + dx, seg_y + dy)
            if segment not in stops_by_segment:
                continue
            # Innermost segments are guaranteed to be in the circle
            if (
                -2 <= dx <= 2
                and -2 <= dy <= 2
                and not ((dx in {-2, 2}) and (dy in {-2, 2}))
            ):
                count += sum(stops_by_segment[segment].values())
                continue
            for stop, stop_count in stops_by_segment[segment].items():
                if (
                    (subway[0] - stop[0]) ** 2 + (subway[1] - stop[1]) ** 2
                ) <= 400:
                    count += stop_count
        if count > max_count:
            max_count = count
            max_subway_index = index
    return max_subway_index + 1


def main():
    n = int(input())
    subways = [tuple(int(s) for s in input().split()) for _ in range(n)]
    m = int(input())
    stops = [tuple(int(s) for s in input().split()) for _ in range(m)]
    print(subway_with_most_stops(subways, stops))  # type: ignore


def reverse_engineer_killer_sequence(subways: Coords, stops: Coords):
    print(f'Subway count: {len(subways)}, unique: {len(set(subways))}')
    min_, max_ = min(subways), max(subways)
    spread = (max_[0] - min_[0], max_[1] - min_[1])
    print(f'min: {min_}, max: {max_}, spread: {spread})')

    print(f'Stop count: {len(stops)}, unique: {len(set(stops))}')
    min_, max_ = min(stops), max(stops)
    spread = (max_[0] - min_[0], max_[1] - min_[1])
    print(f'min: {min_}, max: {max_}, spread: {spread})')


def test_killer_sequence():
    from random import randint, seed
    from time import time

    seed(1)
    s = 165
    c1 = randint(-(10**9), 10**9)
    c2 = randint(-(10**9), 10**9)
    n = 10**4
    subways = [(c1 + randint(-s, s), c2 + randint(-s, s)) for _ in range(n)]
    m = 10**5
    stops = [(c1 + randint(-s, s), c2 + randint(-s, s)) for _ in range(m)]

    now = time()
    print(subway_with_most_stops(subways, stops))
    print(f'{time() - now:.3f} sec')


if __name__ == '__main__':
    main()
