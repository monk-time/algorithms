def count_max_lights(a: list[int], target_count: int) -> tuple[int, list[int]]:
    return 1, [1]


if __name__ == '__main__':
    n, k = [int(s) for s in input().split()]
    a = [int(input()) for _ in range(k)]
    max_count, max_lights = count_max_lights(a, n)
    print(max_count)
    print(*max_lights, sep='\n')
