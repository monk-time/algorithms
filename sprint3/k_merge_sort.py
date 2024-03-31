def merge_sort(a: list[int], left: int, right: int) -> None:
    if right - left <= 1:
        return

    mid = (left + right) // 2
    merge_sort(a, left, mid)
    merge_sort(a, mid, right)
    a[left:right] = merge(a, left, mid, right)


def merge(a: list[int], left: int, mid: int, right: int) -> list[int]:
    result = []
    i, j = left, mid
    while i < mid or j < right:
        if i < mid and (j == right or a[i] <= a[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(a[j])
            j += 1
    return result
