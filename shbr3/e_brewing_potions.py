def max_sum_quality(a: list[int], k: int) -> int:
    return 1


if __name__ == '__main__':
    n, k = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    print(max_sum_quality(a, k))
