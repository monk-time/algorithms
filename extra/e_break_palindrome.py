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


if __name__ == '__main__':
    s = input()
    print(break_palindrome(s))
