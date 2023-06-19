def break_palindrome(s: str) -> str:
    if len(s) <= 1:
        return ''
    chars = list(s)
    for i, char in enumerate(s):
        if char != 'a' and (len(s) % 2 == 0 or i != len(s) // 2):
            chars[i] = 'a'
            break
    else:  # no break
        chars[-1] = 'b'
    return ''.join(chars)


def break_palindrome_func(s: str) -> str:
    if len(s) <= 1:
        return ''
    n = len(s)
    is_not_a_or_mid = lambda i: s[i] != 'a' and (n % 2 == 0 or i != n // 2)
    i = next(filter(is_not_a_or_mid, range(n)), n - 1)
    return s[:i] + ('a' if i != n - 1 else 'b') + s[i + 1 :]


if __name__ == '__main__':
    s = input()
    print(break_palindrome(s))
