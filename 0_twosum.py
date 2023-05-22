def twosum(a, k):
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                return a[i], a[j]
    return [None]


def twosum_with_sort(a, k):
    a.sort()

    left = 0
    right = len(a) - 1
    while left < right:
        current_sum = a[left] + a[right]
        if current_sum == k:
            return a[left], a[right]
        if current_sum < k:
            left += 1
        else:
            right -= 1
    return [None]


n = int(input())
a = list(map(int, input().split()))
k = int(input())
print(' '.join(map(str, twosum(a, k))))
