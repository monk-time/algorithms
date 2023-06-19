def max_substring_with_no_repeatitions(s: str) -> int:
    max_len, chars = 0, {}
    for i, char in enumerate(s):
        if char not in chars:
            chars[char] = i
            continue
        max_len = max(len(chars), max_len)
        for seen_char in list(chars.keys()):
            del chars[seen_char]
            if char == seen_char:
                break
        chars[char] = i
    return max(len(chars), max_len)


if __name__ == '__main__':
    s = input()
    print(max_substring_with_no_repeatitions(s))
