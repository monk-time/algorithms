def is_subsequence(s: str, t: str):
    i = 0
    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
            if i == len(s):
                return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()
    print(is_subsequence(s, t))
