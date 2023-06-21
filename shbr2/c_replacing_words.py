from typing import List


def replace_words(words: List[str], replacements: List[str]) -> List[str]:
    return words


if __name__ == '__main__':
    prefixes = input().split()
    words = input().split()
    print(*replace_words(words, prefixes), sep=' ')
