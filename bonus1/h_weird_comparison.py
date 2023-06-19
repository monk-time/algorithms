def weird_compare(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    # Store indices of first occurence and count
    s_counter, t_counter = {}, {}
    for i in range(len(s)):
        s_char, t_char = s[i], t[i]
        if s_char in s_counter and t_char in t_counter:
            if s_counter[s_char] != t_counter[t_char]:
                return False
            s_counter[s_char][1] += 1
            t_counter[t_char][1] += 1
        elif s_char not in s_counter and t_char not in t_counter:
            s_counter[s_char] = [i, 1]
            t_counter[t_char] = [i, 1]
        else:
            return False
    return True


if __name__ == '__main__':
    s, t = input(), input()
    print('YES' if weird_compare(s, t) else 'NO')
