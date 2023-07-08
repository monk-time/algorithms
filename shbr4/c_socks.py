MAX_VALUE = 10_000


def thickness(socks: list[list[int]], points: list[int]) -> list[int]:
    starts, ends, thicknesses = [[0] * MAX_VALUE for _ in range(3)]
    for start, end in socks:
        starts[start - 1] += 1
        ends[end - 1] += 1
    count = 0
    for i in range(MAX_VALUE):
        count += starts[i]
        thicknesses[i] = count
        count -= ends[i]
    return [thicknesses[p - 1] for p in points]


if __name__ == '__main__':
    max_value, sock_count, point_count = [int(s) for s in input().split()]
    socks = [[int(s) for s in input().split()] for _ in range(sock_count)]
    points = [int(input()) for _ in range(point_count)]
    print(*thickness(socks, points), sep='\n')
