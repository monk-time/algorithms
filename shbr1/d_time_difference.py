from itertools import starmap, pairwise
from operator import sub

DAY = 24 * 60


def to_minutes(time: str) -> int:
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def min_gap(arrivals: list[str]) -> int:
    minutes = sorted(map(to_minutes, arrivals))
    minutes.append(DAY + minutes[0])
    return min(starmap(sub, pairwise(reversed(minutes))))


if __name__ == '__main__':
    n = int(input())
    arrivals = input().split()
    print(min_gap(arrivals))
