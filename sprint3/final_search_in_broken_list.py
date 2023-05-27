from typing import List


def search_in_shifted(a: List[int], value: int) -> int:
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] == value:
            return mid
        if (
            value <= a[mid] <= a[left]
            or a[left] <= value <= a[mid]
            or a[mid] <= a[left] <= value
        ):
            right = mid
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    print(search_in_shifted(a, k))
