MAX_VALUE = 10_000


def thickness(socks: list[list[int]], points: list[int]) -> list[int]:
    count_by_start = [0] * (MAX_VALUE + 1)
    count_by_end = [0] * (MAX_VALUE + 1)
    thicknesses = [0] * (MAX_VALUE + 1)
    for start, end in socks:
        count_by_start[start] += 1
        count_by_end[end] += 1
    count = 0
    for i in range(1, MAX_VALUE + 1):
        count += count_by_start[i]
        thicknesses[i] = count
        count -= count_by_end[i]
    return [thicknesses[i] for i in points]


if __name__ == '__main__':
    max_value, sock_count, point_count = [int(s) for s in input().split()]
    socks = [[int(s) for s in input().split()] for _ in range(sock_count)]
    points = [int(input()) for _ in range(point_count)]
    print(*thickness(socks, points), sep='\n')
