from functools import lru_cache


@lru_cache(maxsize=None)
def count_distinct(n: int) -> int:
    """Count distinct search trees with n unique numbers."""
    if n == 0:
        return 1
    return sum(
        count_distinct(i - 1) * count_distinct(n - i) for i in range(1, n + 1)
    )


if __name__ == '__main__':
    n = int(input())
    print(count_distinct(n))
