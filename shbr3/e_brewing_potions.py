from itertools import accumulate

MAX_QUALITY = 2 * 10**6


def check(
    min_quality: int, prefix_sums: list[int], quality: list[int], k: int
) -> int | None:
    count, total = 0, 0
    for qual in quality:
        if qual < min_quality:
            break
        count += 1
        total += qual
    j = 1
    while j < len(quality) and quality[0] + quality[j] >= min_quality:
        j += 1
    for i in range(len(quality)):
        if i + 1 >= j:
            break
        while j - 1 > i and quality[i] + quality[j - 1] < min_quality:
            j -= 1
        cur_count = j - i - 1
        count += cur_count
        total += prefix_sums[j - 1] - prefix_sums[i] + quality[i] * cur_count
    if count >= k:
        return total - (count - k) * min_quality
    return None


def max_sum_quality(quality: list[int], k: int) -> int | None:
    quality.sort(reverse=True)
    prefix_sums = list(accumulate(quality))
    left, right = -MAX_QUALITY, MAX_QUALITY
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, prefix_sums, quality, k) is None:
            right = mid - 1
        else:
            left = mid
    return check(left, prefix_sums, quality, k)


if __name__ == '__main__':
    n, k = (int(s) for s in input().split())
    quality = [int(s) for s in input().split()]
    print(max_sum_quality(quality, k))
