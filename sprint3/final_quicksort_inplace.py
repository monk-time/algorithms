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


def quicksort_inplace_rec(a: List[int], first: int, last: int) -> None:
    if first >= last:
        return
    pivot = a[(first + last) // 2]
    left, right = first, last
    while True:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1
        if left >= right:
            break
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    quicksort_inplace_rec(a, first, right)
    quicksort_inplace_rec(a, right + 1, last)


def quicksort_inplace(a: List[int]) -> List[int]:
    quicksort_inplace_rec(a, 0, len(a) - 1)
    return a
