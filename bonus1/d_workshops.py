def unique(a: list) -> list:
    return list(dict.fromkeys(a).keys())


if __name__ == '__main__':
    count = int(input())
    a = [input() for _ in range(count)]
    print(*unique(a), sep='\n')
