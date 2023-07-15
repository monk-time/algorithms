def find_peak(mountains: list[int]) -> int:
    prev, i = mountains[0], 1
    while prev <= mountains[i]:
        prev = mountains[i]
        i += 1
    return i


if __name__ == '__main__':
    input()
    mountains = [int(s) for s in input().split()]
    print(find_peak(mountains))
