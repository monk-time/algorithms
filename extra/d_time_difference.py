DAY = 24 * 60


def to_minutes(time: str) -> int:
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def min_gap(arrivals: list[str]) -> int:
    minutes = sorted(map(to_minutes, arrivals))
    min_gap = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))
    if len(minutes) >= 2:
        min_gap = min(min_gap, DAY - minutes[-1] + minutes[0])
    return min_gap


if __name__ == '__main__':
    n = int(input())
    arrivals = input().split()
    print(min_gap(arrivals))
