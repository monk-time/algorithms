"""ID посылки: 88287103."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Participant:
    name: str
    tasks: int
    penalty: int

    @classmethod
    def from_text(cls, text: str):
        name, tasks, penalty = text.split()
        return cls(name=name, tasks=int(tasks), penalty=int(penalty))

    def __lt__(self, other: 'Participant'):
        if not isinstance(other, Participant):
            raise TypeError('Участников можно сравнивать только друг с другом')
        self_key = (-self.tasks, self.penalty, self.name)
        other_key = (-other.tasks, other.penalty, other.name)
        return self_key < other_key

    def __str__(self):
        return self.name


def partition(a: List, left: int, right: int) -> int:
    pivot = a[(left + right) // 2]
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


def quicksort(a: List, left: int = 0, right: Optional[int] = None) -> None:
    if right is None:
        right = len(a) - 1
    if left >= right:
        return
    border = partition(a, left, right)
    quicksort(a, left, border)
    quicksort(a, border + 1, right)


def main():
    count = int(input())
    participants = [Participant.from_text(input()) for _ in range(count)]
    quicksort(participants)
    print(*participants, sep='\n')


if __name__ == '__main__':
    main()
