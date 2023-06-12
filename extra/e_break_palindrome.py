def break_palindrome(s: str) -> str:
    if len(s) <= 1:
        return ''
    s2 = []
    has_changed = False
    for i, char in enumerate(s):
        if (
            char != 'a'
            and not has_changed
            and not (len(s) % 2 != 0 and i == len(s) // 2)
        ):
            s2.append('a')
            has_changed = True
        else:
            s2.append(char)
    if not has_changed:
        s2[-1] = 'b'
    return ''.join(s2)


if __name__ == '__main__':
    s = input()
    print(break_palindrome(s))
