from typing import List
from random import choices


def quicksort(a: List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    pivot = len(a) // 2
    left, right = [], []
    for n in a:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    return quicksort(left) + quicksort(right)


def quicksort_inplace(a: List[int]) -> List[int]:
    pass


a = choices(range(20), k=100)
assert sorted(a) == quicksort(a)
