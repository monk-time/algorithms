from collections import Counter, defaultdict
from typing import List


def anagram_groups(words: List[str]) -> List[List[int]]:
    groups = defaultdict(lambda: [])
    for index, word in enumerate(words):
        key = frozenset(Counter(word).items())
        groups[key].append(index)
    return list(groups.values())


if __name__ == '__main__':
    n = int(input())
    words = input().split()
    groups = anagram_groups(words)
    print(*(' '.join(map(str, group)) for group in groups), sep='\n')
