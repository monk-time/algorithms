"""ID посылки: 88264568."""

from typing import List


def broken_search(nums: List[int], target: int) -> int:
    """Binary search for value in a shifted sorted list.

    In order to choose which half to move to we need to know
    the position of the shift. The shift can be located based
    on the values of the left element (a), the middle (m)
    and the target (t).
    There are six possible arrangements of these three elements,
    and for each arrangement their relative positions are enough
    to make the choice.
    On the diagram of arrangements below the shift is marked as |:

    a--t--|-----m-----------   m <= a <= t   (choose left half)
    a-----|--t--m-----------   t <= m <= a   (choose left half)
    a-----|-----m--t--------   m <= t <= a   (choose right half)
    a--------t--m-----|-----   a <= t <= m   (choose left half)
    a-----------m--t--|-----   a <= m <= t   (choose right half)
    a-----------m-----|--t--   t <= a <= m   (choose right half)
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if (
            nums[mid] <= nums[left] <= target
            or target <= nums[mid] <= nums[left]
            or nums[left] <= target <= nums[mid]
        ):
            right = mid
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    _ = int(input())
    target = int(input())
    nums = list(map(int, input().split()))
    print(broken_search(nums, target))
