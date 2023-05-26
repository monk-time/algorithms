from typing import List


def run_bubble_sort(a: List[int]) -> None:
    is_sorted_at_start = True
    while True:
        is_sorted = True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                is_sorted = is_sorted_at_start = False
        if is_sorted:
            break
        print(*a)
    if is_sorted_at_start:
        print(*a)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    run_bubble_sort(a)
