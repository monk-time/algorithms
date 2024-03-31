from dataclasses import dataclass
from itertools import pairwise


@dataclass
class Dig:
    day: int
    sidewalk: int


def min_sadness(
    digs: list[Dig], sidewalk_count: int, laying_count: int
) -> int:
    dig_days_by_sidewalk = [[] for _ in range(sidewalk_count)]
    for dig in digs:
        dig_days_by_sidewalk[dig.sidewalk - 1].append(dig.day)
    sadness_days = []
    for dig_days in dig_days_by_sidewalk:
        if not dig_days:
            continue
        # The final dig on a sidewalk must be covered,
        # and it should happen on the same day it was dug
        laying_count -= 1
        for day_a, day_b in pairwise(dig_days):
            sadness_days.append(day_b - day_a)
    if laying_count < 0:
        return -1
    sadness_days.sort()
    return sum(sadness_days[: len(sadness_days) - laying_count])


if __name__ == '__main__':
    sidewalk_count, dig_count, laying_count = (int(s) for s in input().split())
    digs = [Dig(*map(int, input().split())) for _ in range(dig_count)]
    print(min_sadness(digs, sidewalk_count, laying_count))
