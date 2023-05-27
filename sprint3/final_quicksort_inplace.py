from typing import List


def quicksort(a: List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    pivot = a.pop(len(a) // 2)
    left, right = [], []
    for n in a:
        if n <= pivot:
            left.append(n)
        else:
            right.append(n)
    return quicksort(left) + [pivot] + quicksort(right)


def partition(a: List[int], start: int, end: int) -> int:
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


def quicksort_inplace_rec(a: List[int], start: int, end: int) -> None:
    if start >= end:
        return
    parts_border = partition(a, start, end)
    quicksort_inplace_rec(a, start, parts_border)
    quicksort_inplace_rec(a, parts_border + 1, end)


def quicksort_inplace(a: List[int]) -> List[int]:
    quicksort_inplace_rec(a, 0, len(a) - 1)
    return a
