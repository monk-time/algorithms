from collections import defaultdict
from collections.abc import Iterable
from functools import reduce

LEAF = object()


def replace_words(words: list[str], prefixes: list[str]) -> Iterable[str]:
    make_tree = lambda: defaultdict(make_tree)
    prefix_tree = make_tree()
    for prefix in prefixes:
        leaf = reduce(lambda tree, ch: tree[ch], prefix, prefix_tree)
        leaf[LEAF] = prefix  # type: ignore
    for word in words:
        subtree = prefix_tree
        for char in word:
            if char not in subtree:
                yield word
                break
            subtree = subtree[char]
            if LEAF in subtree:
                yield subtree[LEAF]
                break
        else:  # no break
            yield word


if __name__ == '__main__':
    prefixes = input().split()
    words = input().split()
    print(*replace_words(words, prefixes), sep=' ')
