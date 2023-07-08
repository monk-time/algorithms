def find_dates(friends: list[list[int]]) -> list[list[int]]:
    dates = sorted((date, index) for index, date in enumerate(friends))
    next_start = 0
    result = [[-1, -1] for _ in range(len(friends))]
    for (start, end), index in dates:
        if next_start > end:
            continue
        result[index] = [max(next_start, start), end]
        next_start = end + 1
    return result


if __name__ == '__main__':
    n = int(input())
    friends = [[int(s) for s in input().split()] for _ in range(n)]
    for date in find_dates(friends):
        print(*date)
