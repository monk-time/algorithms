from collections import Counter, defaultdict


def anagram_groups(words: list[str]) -> list[list[int]]:
    groups = defaultdict(list)
    for index, word in enumerate(words):
        key = frozenset(Counter(word).items())
        groups[key].append(index)
    return list(groups.values())


if __name__ == '__main__':
    n = int(input())
    words = input().split()
    groups = anagram_groups(words)
    print(*(' '.join(map(str, group)) for group in groups), sep='\n')
