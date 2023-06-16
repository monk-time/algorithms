def median(a):
    half, remainder = divmod(len(a), 2)
    if remainder != 0 or a[half - 1] == a[half]:
        return a[half]
    avg, remainder = divmod(a[half - 1] + a[half], 2)
    return avg if not remainder else avg + 0.5


def median_two(a, b):
    a_left, a_right = 0, len(a) - 1
    b_left, b_right = 0, len(b) - 1
    while a_left <= a_right and b_left <= b_right:
        if a_left == a_right and b_left == b_right:
            avg, remainder = divmod(a[a_left] + b[b_left], 2)
            return avg if not remainder else avg + 0.5
        if a[a_left] <= b[b_left]:
            a_left += 1
        else:
            b_left += 1
        if a[a_right] >= b[b_right]:
            a_right -= 1
        else:
            b_right -= 1
    return median(
        a[a_left : a_right + 1]
        if a_left <= a_right
        else b[b_left : b_right + 1]
    )


if __name__ == '__main__':
    _, _ = input(), input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(median_two(a, b))
