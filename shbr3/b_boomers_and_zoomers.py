def count_invitations(a: list[int]) -> int:
    if len(a) <= 1:
        return 0
    a = sorted(a)
    left, right_first, right = 0, 0, 0
    count = 0
    # j invites i iff 0.5 * a[j] + 7 < a[i] <= a[j]
    while right < len(a):
        if a[right] > a[right_first]:
            right_first = right
        while left < right and 0.5 * a[right] + 7 >= a[left]:
            left += 1
        if a[left] > 14:
            count += (right - left) + (right - right_first)
        right += 1
    return count


def count_invitations_bruteforce(a: list[int]) -> int:
    count = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if 0.5 * a[i] + 7 < a[j] <= a[i]:
                count += 1
            if 0.5 * a[j] + 7 < a[i] <= a[j]:
                count += 1
    return count


if __name__ == '__main__':
    # _ = input()
    # ages = [int(s) for s in input().split()]
    # print(count_invitations(ages))

    import random

    while True:
        a = random.choices(range(1, 121), k=10)
        res = count_invitations(a)
        res_true = count_invitations_bruteforce(a)
        if res != res_true:
            print(f'{a=}, {res=}, {res_true=}')
