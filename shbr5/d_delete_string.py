def min_length_after_ops(s: str) -> int:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return right - left + 1
        char = s[left]
        while left < len(s) and s[left] == char:
            left += 1
        while right >= 0 and s[right] == char:
            right -= 1
    return 0 if left > right else 1


if __name__ == '__main__':
    s = input()
    print(min_length_after_ops(s))
