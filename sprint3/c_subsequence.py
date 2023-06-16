def is_subsequence(a: str, b: str):
    i = 0
    for j in range(len(b)):
        if a[i] == b[j]:
            i += 1
            if i == len(a):
                return True
    return False


def is_subsequence_rec(a: str, b: str):
    if not a:
        return True
    if not b:
        return False
    if a[0] == b[0]:
        return is_subsequence_rec(a[1:], b[1:])
    return is_subsequence_rec(a, b[1:])


if __name__ == '__main__':
    a, b = input(), input()
    print(is_subsequence(a, b))
