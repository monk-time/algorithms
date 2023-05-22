from collections import Counter


def extra_letter(s: str, t: str) -> str:
    diff = Counter(t) - Counter(s)
    return diff.most_common(1)[0][0]


if __name__ == '__main__':
    s = input()
    t = input()
    print(extra_letter(s, t))
