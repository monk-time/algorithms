def has_repeats_at_dist(a: list[int], max_dist: int) -> bool:
    last_seen = {}
    for index, item in enumerate(a):
        if item in last_seen and index - last_seen[item] <= max_dist:
            return True
        last_seen[item] = index
    return False


if __name__ == '__main__':
    n, max_dist = (int(s) for s in input().split())
    a = [int(s) for s in input().split()]
    print('YES' if has_repeats_at_dist(a, max_dist) else 'NO')
