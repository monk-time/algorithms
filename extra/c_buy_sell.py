from random import randint


def find_max_difference(a: list[int], money: int = 1000) -> tuple[int, int]:
    max_i, max_j, max_diff = 0, 0, 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > money:
                continue
            gas = money // a[i]
            new_diff = gas * (a[j] - a[i])
            if a[i] <= money and new_diff > max_diff:
                max_i, max_j = i + 1, j + 1
                max_diff = new_diff
    return max_i, max_j


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    # numbers = [randint(1, 5001) for _ in range(100_000)]
    print(*find_max_difference(numbers), sep=' ')
