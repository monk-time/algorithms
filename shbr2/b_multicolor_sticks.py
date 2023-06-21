import re
from collections import defaultdict


def count_sticks(s: str) -> int:
    sticks = defaultdict(set)
    for color, num in re.findall(r'\w\d', s):
        sticks[num].add(color)
    return sum(len(stick) == 3 for stick in sticks.values())


if __name__ == '__main__':
    s = input()
    print(count_sticks(s))
