from typing import List, Tuple


def find_sum_groups_slow(
    nums: List[int], target: int
) -> List[Tuple[int, ...]]:
    result = []
    nums.sort()
    stack: List[Tuple[int, List[int], int]] = [(0, [], target)]

    while stack:
        start, path, remaining = stack.pop()
        if len(path) == 4:
            if not remaining:
                result.append(tuple(path))
            continue
        for i in range(start, len(nums)):
            if nums[i] > 0 and nums[i] > remaining:
                break
            stack.append((i + 1, path + [nums[i]], remaining - nums[i]))

    return sorted(set(result))


def find_sum_groups(nums: List[int], target: int) -> List[Tuple[int, ...]]:
    result = []
    nums.sort()
    cycles = 0

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            remaining = target - nums[i] - nums[j]
            left = j + 1
            right = len(nums) - 1

            while left < right:
                cycles += 1
                current_sum = nums[left] + nums[right]
                if current_sum < remaining:
                    left += 1
                elif current_sum > remaining:
                    right -= 1
                else:
                    result.append((nums[i], nums[j], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
    print(cycles)
    return result


if __name__ == '__main__':
    from random import choices
    from time import time

    max_abs = 1000
    target = 0
    a = choices(range(-max_abs, max_abs + 1), k=600)

    now = time()
    sum_groups = find_sum_groups(a, target)
    print(f'{len(sum_groups)} groups')
    print(f'{time() - now} sec')

    # n = int(input())
    # target = int(input())
    # a = [int(s) for s in input().split()]
    # sum_groups = find_sum_groups(a, target)
    # print(len(sum_groups))
    # for sum_group in sum_groups:
    #     print(*sum_group)
