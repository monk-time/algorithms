from collections import Counter


def top_k_schools(schools: list[int], k: int) -> list[int]:
    counter = Counter(schools)
    by_freq_value = lambda t: (-t[1], t[0])
    top_schools = sorted(counter.items(), key=by_freq_value)
    return [t[0] for t in top_schools][:k]


if __name__ == '__main__':
    n = int(input())
    schools = list(map(int, input().split()))
    k = int(input())
    print(*top_k_schools(schools, k))
