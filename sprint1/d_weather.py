def calc_chaos(temps: list[int]) -> int:
    n = len(temps)
    return sum(
        (i == 0 or temps[i] > temps[i - 1])
        and (i == n - 1 or temps[i] > temps[i + 1])
        for i in range(n)
    )


if __name__ == '__main__':
    _ = int(input())
    temps = [int(s) for s in input().split()]
    print(calc_chaos(temps))
