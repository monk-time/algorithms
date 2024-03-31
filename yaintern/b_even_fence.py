def min_minmax_diff(lengths: list[int], extra: int) -> int:
    lengths.sort()
    count = len(lengths) - extra
    diffs = sorted(
        lengths[i + count - 1] - lengths[i] for i in range(extra + 1)
    )
    return diffs[0]


if __name__ == '__main__':
    count, extra = (int(s) for s in input().split())
    lengths = [int(s) for s in input().split()]
    print(min_minmax_diff(lengths, extra))
