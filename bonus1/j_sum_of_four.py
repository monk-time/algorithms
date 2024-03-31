from collections import defaultdict


def find_sum_groups(nums: list[int], target: int) -> list[tuple[int, ...]]:  # noqa: C901
    nums.sort()
    two_sums = defaultdict(list)
    result = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            two_sum = nums[i] + nums[j]
            two_sums[two_sum].append([i, j])
    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            two_sum = nums[i] + nums[j]
            if target - two_sum not in two_sums:
                continue
            for m, n in two_sums[target - two_sum]:
                if m <= j:
                    continue
                group = (nums[i], nums[j], nums[m], nums[n])
                if not result or result[-1] != group:
                    result.append(group)
    return result


if __name__ == '__main__':
    n = int(input())
    target = int(input())
    a = [int(s) for s in input().split()]
    sum_groups = find_sum_groups(a, target)
    print(len(sum_groups))
    for sum_group in sum_groups:
        print(*sum_group)
