def max_perimeter(lens: list[int]) -> int | None:
    lens.sort(reverse=True)
    for i in range(len(lens) - 2):
        c, b, a = lens[i : i + 3]
        if c < a + b:
            return a + b + c
    return None


if __name__ == '__main__':
    n = int(input())
    lens = list(map(int, input().split()))
    print(max_perimeter(lens))
