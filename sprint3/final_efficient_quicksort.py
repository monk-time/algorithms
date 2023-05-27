from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Participant:
    name: str
    tasks: int
    penalty: int

    @classmethod
    def from_text(cls, s: str):
        name, tasks, penalty = s.split()
        return cls(name=name, tasks=int(tasks), penalty=int(penalty))

    def __lt__(self, other: 'Participant'):
        if not isinstance(other, Participant):
            raise TypeError('Участников можно сравнивать только друг с другом')
        self_key = (-self.tasks, self.penalty, self.name)
        other_key = (-other.tasks, other.penalty, other.name)
        return self_key < other_key

    def __str__(self):
        return self.name


def partition(a: List, start: int, end: int) -> int:
    pivot = a[(start + end) // 2]
    left, right = start, end
    while True:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1
        if left >= right:
            return right
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1


def quicksort(a: List, start: int = 0, end: Optional[int] = None) -> None:
    if end is None:
        end = len(a) - 1
    if start >= end:
        return
    parts_border = partition(a, start, end)
    quicksort(a, start, parts_border)
    quicksort(a, parts_border + 1, end)


def main():
    n = int(input())
    participants = [Participant.from_text(input()) for _ in range(n)]
    quicksort(participants)
    print(*participants, sep='\n')


if __name__ == '__main__':
    main()
