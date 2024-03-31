def prefix_hashes(a: int, m: int, s: str) -> list[int]:
    # Can be even shorter with itertools.accumulate
    result, hash_ = [], 0
    for ch in s:
        hash_ = (hash_ * a + ord(ch)) % m
        result.append(hash_)
    return result


def substring_hash(a: int, m: int, prefixes: list[int], i: int, j: int) -> int:
    if not i:
        return prefixes[j]
    return (prefixes[j] - pow(a, j - i + 1, m) * prefixes[i - 1]) % m


def main():
    a = int(input())
    m = int(input())
    s = input()
    count = int(input())
    prefixes = prefix_hashes(a, m, s)
    for _ in range(count):
        i, j = (int(s) for s in input().split())
        print(substring_hash(a, m, prefixes, i - 1, j - 1))


if __name__ == '__main__':
    main()
