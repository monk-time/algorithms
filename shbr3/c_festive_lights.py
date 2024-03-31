from itertools import chain, repeat
from math import ceil


def make_x_same_lights(
    sorted_counts: tuple[int], lights_len: int, x: int
) -> tuple[int] | None:
    used_counts = []
    total = 0
    for count in sorted_counts:
        used = min(count // x, lights_len - total)
        if not used:
            break
        used_counts.append(used)
        total += used
    return tuple(used_counts) if total == lights_len else None


def count_max_lights(
    counts: tuple[int, ...], lights_len: int
) -> tuple[int, tuple[int, ...]]:
    enumerated_counts = sorted(
        zip(counts, range(len(counts))),
        key=lambda t: (-t[0], t[1]),
    )
    sorted_counts, original_indices = zip(*enumerated_counts)

    left, right = 1, sorted_counts[0]
    while left <= right:
        if left == right:
            break
        mid = ceil((left + right) / 2)
        if make_x_same_lights(sorted_counts, lights_len, mid):
            left = mid
        else:
            right = mid - 1

    lights = make_x_same_lights(sorted_counts, lights_len, left)
    if not lights:
        return 0, ()
    return left, tuple(
        chain.from_iterable(
            repeat(original_indices[index] + 1, count)
            for index, count in enumerate(lights)
        )
    )


if __name__ == '__main__':
    n, k = (int(s) for s in input().split())
    a = tuple(int(input()) for _ in range(k))
    max_count, max_lights = count_max_lights(a, n)
    print(max_count)
    print(*max_lights, sep='\n')
