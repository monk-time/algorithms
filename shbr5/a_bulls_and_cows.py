from collections import Counter


def count_bulls_and_cows(a: str, b: str) -> tuple[int, int]:
    bulls, cows = 0, 0
    counter = Counter(a)
    for i in range(len(a)):
        if a[i] == b[i]:
            bulls += 1
            counter[b[i]] -= 1
    for i in range(len(a)):
        if a[i] != b[i] and counter[b[i]]:
            cows += 1
            counter[b[i]] -= 1
    return bulls, cows


if __name__ == '__main__':
    a, b = input(), input()
    print(*count_bulls_and_cows(a, b), sep='\n')
